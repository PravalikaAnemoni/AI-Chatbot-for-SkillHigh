# Advanced AI Chatbot for SkillHigh
import pandas as pd
import numpy as np
import pickle
import re
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.naive_bayes import MultinomialNB
from textblob import TextBlob
from googletrans import Translator
import nltk
from nltk.corpus import stopwords
from nltk.tokenize import word_tokenize
from nltk.stem import WordNetLemmatizer
import warnings
warnings.filterwarnings('ignore')

# Download required NLTK data
try:
    nltk.data.find('tokenizers/punkt')
    nltk.data.find('corpora/stopwords')
    nltk.data.find('corpora/wordnet')
except LookupError:
    nltk.download('punkt')
    nltk.download('stopwords')
    nltk.download('wordnet')

class SkillHighChatbot:
    def __init__(self):
        self.vectorizer = TfidfVectorizer(max_features=1000, stop_words='english')
        self.intent_classifier = MultinomialNB()
        self.lemmatizer = WordNetLemmatizer()
        self.translator = Translator()
        self.session_memory = {}
        self.conversation_history = {}
        self.is_trained = False
        
    def preprocess_text(self, text):
        """Preprocess text for better understanding"""
        # Convert to lowercase
        text = str(text).lower()
        
        # Simple preprocessing - just lowercase and basic cleaning
        text = re.sub(r'[^\w\s]', ' ', text)  # Keep alphanumeric and spaces
        text = re.sub(r'\s+', ' ', text)      # Replace multiple spaces with single space
        text = text.strip()
        
        # If text is too short, return as is
        if len(text) < 2:
            return text
        
        return text
    
    def train_model(self, data_path):
        """Train the intent classification model"""
        try:
            # Load training data
            df = pd.read_csv(data_path)
            
            # Clean the data - remove any rows with NaN values
            df = df.dropna()
            
            # Ensure all text columns are strings
            df['Text'] = df['Text'].astype(str)
            df['Intent'] = df['Intent'].astype(str)
            df['Response'] = df['Response'].astype(str)
            
            # Preprocess texts
            df['processed_text'] = df['Text'].apply(self.preprocess_text)
            
            # Prepare features and labels
            X = self.vectorizer.fit_transform(df['processed_text'])
            y = df['Intent']
            
            # Train the classifier
            self.intent_classifier.fit(X, y)
            self.is_trained = True
            
            # Store responses for quick lookup - handle duplicates
            response_dict = {}
            for _, row in df.iterrows():
                intent = row['Intent']
                response = row['Response']
                if intent not in response_dict:
                    response_dict[intent] = response
            self.responses = response_dict
            
            print("Model trained successfully!")
            return True
            
        except Exception as e:
            print(f"Error training model: {e}")
            return False
    
    def predict_intent(self, text):
        """Predict intent from user input"""
        if not self.is_trained:
            return "Unknown", 0.0
        
        processed_text = self.preprocess_text(text)
        X = self.vectorizer.transform([processed_text])
        intent = self.intent_classifier.predict(X)[0]
        confidence = self.intent_classifier.predict_proba(X).max()
        
        # Fallback for simple greetings with low confidence
        if confidence < 0.3:
            text_lower = processed_text.lower().strip()
            greeting_words = ['hi', 'hello', 'hey', 'hii', 'hlo', 'good morning', 'good afternoon', 'good evening']
            if any(word in text_lower for word in greeting_words):
                return "Greeting", 0.8
        
        return intent, confidence
    
    def analyze_sentiment(self, text):
        """Analyze sentiment of user input"""
        blob = TextBlob(text)
        sentiment = blob.sentiment.polarity
        
        if sentiment > 0.1:
            return "positive"
        elif sentiment < -0.1:
            return "negative"
        else:
            return "neutral"
    
    def translate_text(self, text, target_lang='hi'):
        """Translate text to target language"""
        try:
            result = self.translator.translate(text, dest=target_lang)
            return result.text
        except:
            return text
    
    def get_contextual_response(self, intent, sentiment, user_id=None):
        """Get response based on intent and sentiment"""
        base_response = self.responses.get(intent, "I'm sorry, I didn't understand that. Could you please rephrase?")
        
        # Add empathetic responses based on sentiment
        if sentiment == "negative":
            empathy_prefixes = [
                "I understand your concern. ",
                "I'm here to help with that. ",
                "Let me clarify that for you. "
            ]
            import random
            base_response = random.choice(empathy_prefixes) + base_response
        
        return base_response
    
    def update_session_memory(self, user_id, intent, response):
        """Update session memory for contextual conversations"""
        if user_id not in self.session_memory:
            self.session_memory[user_id] = []
        
        self.session_memory[user_id].append({
            'intent': intent,
            'response': response,
            'timestamp': pd.Timestamp.now()
        })
        
        # Keep only last 5 interactions
        if len(self.session_memory[user_id]) > 5:
            self.session_memory[user_id] = self.session_memory[user_id][-5:]
    
    def get_response(self, message, user_id="default", language="en"):
        """Main function to get chatbot response"""
        try:
            # Translate input if needed
            if language != "en":
                message = self.translate_text(message, target_lang='en')
            
            # Predict intent
            intent, confidence = self.predict_intent(message)
            
            # Analyze sentiment
            sentiment = self.analyze_sentiment(message)
            
            # Get contextual response
            response = self.get_contextual_response(intent, sentiment, user_id)
            
            # Update session memory
            self.update_session_memory(user_id, intent, response)
            
            # Translate response if needed
            if language != "en":
                response = self.translate_text(response, target_lang=language)
            
            return {
                'response': response,
                'intent': intent,
                'confidence': confidence,
                'sentiment': sentiment
            }
            
        except Exception as e:
            return {
                'response': "I'm sorry, I encountered an error. Please try again.",
                'intent': 'Error',
                'confidence': 0.0,
                'sentiment': 'neutral'
            }

# Global chatbot instance
chatbot = SkillHighChatbot()

def get_response(message, user_id="default", language="en"):
    """Wrapper function for backward compatibility"""
    result = chatbot.get_response(message, user_id, language)
    return result['response']

def initialize_chatbot():
    """Initialize and train the chatbot"""
    data_path = "data/intents.csv"
    return chatbot.train_model(data_path)

def get_chatbot():
    """Get the chatbot instance"""
    return chatbot