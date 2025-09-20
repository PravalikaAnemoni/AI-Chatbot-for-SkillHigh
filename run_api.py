# Simple API runner for SkillHigh Chatbot

import sys
import os

# Add the current directory to Python path
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

# Import and run the API
from app.api import app

if __name__ == '__main__':
    print("🤖 Starting SkillHigh Chatbot API...")
    print("API Endpoints:")
    print("- POST /chat - Main chat endpoint")
    print("- GET /analytics - Usage analytics")
    print("- GET /health - Health check")
    print("- GET /session/<user_id> - Get session history")
    print("- DELETE /session/<user_id> - Clear session")
    print("\nAPI will be available at: http://localhost:5000")
    print("Press Ctrl+C to stop the server")
    
    try:
        app.run(debug=True, host='0.0.0.0', port=5000)
    except KeyboardInterrupt:
        print("\n👋 API server stopped. Goodbye!")
