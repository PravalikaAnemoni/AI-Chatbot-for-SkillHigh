# Flask REST API for SkillHigh Chatbot

import sys
import os
sys.path.append(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))

from flask import Flask, request, jsonify
from flask_cors import CORS
from app.chatbot import get_chatbot, initialize_chatbot
import json
from datetime import datetime

app = Flask(__name__)
CORS(app)  # Enable CORS for web integration

# Initialize chatbot on startup
chatbot = get_chatbot()
initialize_chatbot()

# Analytics storage (in production, use a proper database)
analytics_data = {
    'total_conversations': 0,
    'intent_counts': {},
    'sentiment_counts': {'positive': 0, 'negative': 0, 'neutral': 0},
    'language_usage': {'en': 0, 'hi': 0},
    'daily_stats': {}
}

@app.route('/', methods=['GET'])
def home():
    """Home endpoint with API information"""
    return jsonify({
        "message": "Welcome to SkillHigh AI Chatbot API!",
        "version": "1.0.0",
        "endpoints": {
            "POST /chat": "Main chat endpoint",
            "GET /analytics": "Usage analytics",
            "GET /health": "Health check",
            "GET /session/<user_id>": "Get session history",
            "DELETE /session/<user_id>": "Clear session"
        },
        "status": "running"
    })

@app.route('/chat', methods=['POST'])
def chat():
    """Main chat endpoint with enhanced features"""
    try:
        data = request.json
        user_input = data.get("message", "")
        user_id = data.get("user_id", "anonymous")
        language = data.get("language", "en")
        
        if not user_input.strip():
            return jsonify({
                "reply": "Please enter a message.",
                "intent": "Empty",
                "confidence": 0.0,
                "sentiment": "neutral"
            })
        
        # Get chatbot response
        result = chatbot.get_response(user_input, user_id, language)
        
        # Update analytics
        update_analytics(result, language)
        
        return jsonify(result)
        
    except Exception as e:
        return jsonify({
            "reply": "I'm sorry, I encountered an error. Please try again.",
            "intent": "Error",
            "confidence": 0.0,
            "sentiment": "neutral",
            "error": str(e)
        })

@app.route('/analytics', methods=['GET'])
def get_analytics():
    """Get chatbot usage analytics"""
    return jsonify(analytics_data)

@app.route('/health', methods=['GET'])
def health_check():
    """Health check endpoint"""
    return jsonify({
        "status": "healthy",
        "model_trained": chatbot.is_trained,
        "timestamp": datetime.now().isoformat()
    })

@app.route('/session/<user_id>', methods=['GET'])
def get_session_history(user_id):
    """Get conversation history for a user"""
    if user_id in chatbot.session_memory:
        return jsonify(chatbot.session_memory[user_id])
    return jsonify([])

@app.route('/session/<user_id>', methods=['DELETE'])
def clear_session(user_id):
    """Clear conversation history for a user"""
    if user_id in chatbot.session_memory:
        del chatbot.session_memory[user_id]
    return jsonify({"message": "Session cleared"})

def update_analytics(result, language):
    """Update analytics data"""
    global analytics_data
    
    analytics_data['total_conversations'] += 1
    
    # Update intent counts
    intent = result.get('intent', 'Unknown')
    analytics_data['intent_counts'][intent] = analytics_data['intent_counts'].get(intent, 0) + 1
    
    # Update sentiment counts
    sentiment = result.get('sentiment', 'neutral')
    analytics_data['sentiment_counts'][sentiment] += 1
    
    # Update language usage
    analytics_data['language_usage'][language] += 1
    
    # Update daily stats
    today = datetime.now().strftime('%Y-%m-%d')
    if today not in analytics_data['daily_stats']:
        analytics_data['daily_stats'][today] = 0
    analytics_data['daily_stats'][today] += 1

if __name__ == '__main__':
    print("Starting SkillHigh Chatbot API...")
    print("API Endpoints:")
    print("- POST /chat - Main chat endpoint")
    print("- GET /analytics - Usage analytics")
    print("- GET /health - Health check")
    print("- GET /session/<user_id> - Get session history")
    print("- DELETE /session/<user_id> - Clear session")
    app.run(debug=True, host='0.0.0.0', port=5000)