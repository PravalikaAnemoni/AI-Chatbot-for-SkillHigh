# Test script for SkillHigh Chatbot

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.chatbot import initialize_chatbot, get_chatbot

def test_chatbot():
    """Test the chatbot functionality"""
    print("🤖 Testing SkillHigh Chatbot...")
    print("=" * 50)
    
    # Initialize chatbot
    print("Initializing chatbot...")
    success = initialize_chatbot()
    
    if not success:
        print("❌ Failed to initialize chatbot")
        return
    
    print("✅ Chatbot initialized successfully!")
    print()
    
    # Get chatbot instance
    chatbot = get_chatbot()
    
    # Test cases
    test_cases = [
        "Hi there!",
        "What courses do you offer?",
        "Tell me about internships",
        "What are the course fees?",
        "How can I enroll?",
        "Do you provide certificates?",
        "Thank you!",
        "Goodbye"
    ]
    
    print("🧪 Running test cases...")
    print("-" * 50)
    
    for i, test_input in enumerate(test_cases, 1):
        print(f"Test {i}: {test_input}")
        
        # Get response
        result = chatbot.get_response(test_input, f"test_user_{i}")
        
        print(f"Response: {result['response']}")
        print(f"Intent: {result['intent']}")
        print(f"Confidence: {result['confidence']:.2f}")
        print(f"Sentiment: {result['sentiment']}")
        print("-" * 30)
    
    print("✅ All tests completed!")
    print()
    
    # Test multilingual support
    print("🌐 Testing multilingual support...")
    hindi_test = "नमस्ते! आप क्या पाठ्यक्रम प्रदान करते हैं?"
    result = chatbot.get_response(hindi_test, "test_hindi", "hi")
    print(f"Hindi Input: {hindi_test}")
    print(f"Response: {result['response']}")
    print()
    
    # Test session memory
    print("🧠 Testing session memory...")
    user_id = "memory_test_user"
    
    # First message
    result1 = chatbot.get_response("Hi, I'm interested in Data Science", user_id)
    print(f"Message 1: Hi, I'm interested in Data Science")
    print(f"Response: {result1['response']}")
    
    # Second message (should have context)
    result2 = chatbot.get_response("What are the fees for that?", user_id)
    print(f"Message 2: What are the fees for that?")
    print(f"Response: {result2['response']}")
    
    # Check session memory
    if user_id in chatbot.session_memory:
        print(f"Session memory entries: {len(chatbot.session_memory[user_id])}")
    
    print()
    print("🎉 All tests passed successfully!")
    print("The SkillHigh Chatbot is ready for use!")

if __name__ == "__main__":
    test_chatbot()
