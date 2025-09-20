# Streamlit Demo App for SkillHigh Chatbot

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

import streamlit as st
import requests
import json
import plotly.express as px
import plotly.graph_objects as go
from datetime import datetime, timedelta
import pandas as pd

# Page configuration
st.set_page_config(
    page_title="SkillHigh AI Chatbot",
    page_icon="🤖",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Custom CSS
st.markdown("""
<style>
    .main-header {
        font-size: 3rem;
        color: #1f77b4;
        text-align: center;
        margin-bottom: 2rem;
    }
    .chat-message {
        padding: 1rem;
        border-radius: 10px;
        margin: 1rem 0;
        border-left: 4px solid #1f77b4;
        color: #333333;
        font-weight: 500;
    }
    .user-message {
        background-color: #007bff;
        color: white;
        border-left-color: #0056b3;
        margin-left: 20%;
        margin-right: 5%;
    }
    .bot-message {
        background-color: #28a745;
        color: white;
        border-left-color: #1e7e34;
        margin-left: 5%;
        margin-right: 20%;
    }
    .metric-card {
        background-color: #f8f9fa;
        padding: 1rem;
        border-radius: 10px;
        border: 1px solid #dee2e6;
    }
    .chat-message strong {
        color: inherit;
        font-weight: bold;
    }
    .chat-message small {
        color: rgba(255, 255, 255, 0.8);
        font-size: 0.8em;
    }
</style>
""", unsafe_allow_html=True)

# Initialize session state
if 'messages' not in st.session_state:
    st.session_state.messages = []
if 'user_id' not in st.session_state:
    st.session_state.user_id = f"user_{datetime.now().strftime('%Y%m%d_%H%M%S')}"
if 'api_url' not in st.session_state:
    st.session_state.api_url = "http://localhost:5000"

def send_message(message, language="en"):
    """Send message to chatbot API"""
    try:
        response = requests.post(
            f"{st.session_state.api_url}/chat",
            json={
                "message": message,
                "user_id": st.session_state.user_id,
                "language": language
            },
            timeout=10
        )
        return response.json()
    except requests.exceptions.RequestException as e:
        return {
            "response": "Sorry, I'm having trouble connecting to the server. Please make sure the API is running.",
            "intent": "Error",
            "confidence": 0.0,
            "sentiment": "neutral"
        }

def get_analytics():
    """Get analytics data from API"""
    try:
        response = requests.get(f"{st.session_state.api_url}/analytics", timeout=5)
        return response.json()
    except:
        return None

def main():
    # Header
    st.markdown('<h1 class="main-header">🤖 SkillHigh AI Chatbot</h1>', unsafe_allow_html=True)
    
    # Sidebar
    with st.sidebar:
        st.header("⚙️ Settings")
        
        # Language selection
        language = st.selectbox(
            "Language / भाषा",
            ["en", "hi"],
            format_func=lambda x: "English" if x == "en" else "हिंदी"
        )
        
        # API URL configuration
        st.subheader("🔧 API Configuration")
        api_url = st.text_input("API URL", value=st.session_state.api_url)
        if api_url != st.session_state.api_url:
            st.session_state.api_url = api_url
        
        # Clear conversation
        if st.button("🗑️ Clear Conversation"):
            st.session_state.messages = []
            st.rerun()
        
        # User ID display
        st.subheader("👤 Session Info")
        st.text(f"User ID: {st.session_state.user_id}")
        
        # Quick actions
        st.subheader("🚀 Quick Actions")
        quick_questions = [
            "What courses do you offer?",
            "Tell me about internships",
            "What are the course fees?",
            "How can I enroll?",
            "Do you provide certificates?"
        ]
        
        for question in quick_questions:
            if st.button(f"💬 {question}", key=f"quick_{question}"):
                response = send_message(question, language)
                st.session_state.messages.append({
                    "role": "user",
                    "content": question,
                    "timestamp": datetime.now()
                })
                st.session_state.messages.append({
                    "role": "assistant",
                    "content": response["response"],
                    "intent": response.get("intent", "Unknown"),
                    "confidence": response.get("confidence", 0.0),
                    "sentiment": response.get("sentiment", "neutral"),
                    "timestamp": datetime.now()
                })
                st.rerun()
    
    # Main chat interface
    st.subheader("💬 Chat with SkillHigh Assistant")
    
    # Display chat messages
    for message in st.session_state.messages:
        if message["role"] == "user":
            st.markdown(f"""
            <div class="chat-message user-message">
                <strong>You:</strong> {message["content"]}
                <br><small>{message["timestamp"].strftime("%H:%M:%S")}</small>
            </div>
            """, unsafe_allow_html=True)
        else:
            st.markdown(f"""
            <div class="chat-message bot-message">
                <strong>🤖 SkillHigh Assistant:</strong> {message["content"]}
                <br><small>{message["timestamp"].strftime("%H:%M:%S")} | 
                Intent: {message.get("intent", "Unknown")} | 
                Confidence: {message.get("confidence", 0.0):.2f} | 
                Sentiment: {message.get("sentiment", "neutral")}</small>
            </div>
            """, unsafe_allow_html=True)
    
    # Chat input (outside of columns)
    user_input = st.chat_input("Type your message here...")
    
    if user_input:
        # Add user message
        st.session_state.messages.append({
            "role": "user",
            "content": user_input,
            "timestamp": datetime.now()
        })
        
        # Get bot response
        with st.spinner("Thinking..."):
            response = send_message(user_input, language)
        
        # Add bot response
        st.session_state.messages.append({
            "role": "assistant",
            "content": response["response"],
            "intent": response.get("intent", "Unknown"),
            "confidence": response.get("confidence", 0.0),
            "sentiment": response.get("sentiment", "neutral"),
            "timestamp": datetime.now()
        })
        
        st.rerun()
    
    # Analytics section
    st.markdown("---")
    st.subheader("📊 Chat Analytics")
    
    col1, col2 = st.columns(2)
    
    with col1:
        # Get analytics data
        analytics = get_analytics()
        
        if analytics:
            # Total conversations
            st.metric("Total Conversations", analytics.get("total_conversations", 0))
            
            # Intent distribution
            intent_counts = analytics.get("intent_counts", {})
            if intent_counts:
                st.subheader("🎯 Intent Distribution")
                intent_df = pd.DataFrame(list(intent_counts.items()), columns=["Intent", "Count"])
                fig_intent = px.pie(intent_df, values="Count", names="Intent", title="Intent Distribution")
                st.plotly_chart(fig_intent, use_container_width=True)
        else:
            st.warning("Analytics data not available. Make sure the API is running.")
    
    with col2:
        if analytics:
            # Sentiment analysis
            sentiment_counts = analytics.get("sentiment_counts", {})
            if sentiment_counts:
                st.subheader("😊 Sentiment Analysis")
                sentiment_df = pd.DataFrame(list(sentiment_counts.items()), columns=["Sentiment", "Count"])
                fig_sentiment = px.bar(sentiment_df, x="Sentiment", y="Count", 
                                     color="Sentiment", 
                                     color_discrete_map={"positive": "green", "negative": "red", "neutral": "blue"})
                st.plotly_chart(fig_sentiment, use_container_width=True)
            
            # Language usage
            language_usage = analytics.get("language_usage", {})
            if language_usage:
                st.subheader("🌐 Language Usage")
                for lang, count in language_usage.items():
                    lang_name = "English" if lang == "en" else "हिंदी"
                    st.metric(f"{lang_name} Messages", count)
    
    # Footer
    st.markdown("---")
    st.markdown("""
    <div style="text-align: center; color: #666;">
        <p>🤖 SkillHigh AI Chatbot | Powered by Advanced NLP & Machine Learning</p>
        <p>Built with ❤️ for the SkillHigh AI/ML Challenge</p>
    </div>
    """, unsafe_allow_html=True)

if __name__ == "__main__":
    main()