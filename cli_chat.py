# Command Line Interface for SkillHigh Chatbot

import sys
import os
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from app.chatbot import initialize_chatbot, get_chatbot

def main():
    """Command line chat interface"""
    print("🤖 SkillHigh AI Chatbot - Command Line Interface")
    print("=" * 50)
    print("Type 'quit' or 'exit' to end the conversation")
    print("Type 'help' for available commands")
    print("=" * 50)
    
    # Initialize chatbot
    print("Initializing chatbot...")
    success = initialize_chatbot()
    
    if not success:
        print("❌ Failed to initialize chatbot. Please check your setup.")
        return
    
    print("✅ Chatbot ready!")
    print()
    
    # Get chatbot instance
    chatbot = get_chatbot()
    user_id = "cli_user"
    
    # Main chat loop
    while True:
        try:
            # Get user input
            user_input = input("\n👤 You: ").strip()
            
            # Check for exit commands
            if user_input.lower() in ['quit', 'exit', 'bye']:
                print("🤖 SkillHigh Assistant: Goodbye! Have a great day!")
                break
            
            # Check for help command
            if user_input.lower() == 'help':
                print_help()
                continue
            
            # Check for empty input
            if not user_input:
                print("🤖 SkillHigh Assistant: Please enter a message.")
                continue
            
            # Get chatbot response
            print("🤖 SkillHigh Assistant: ", end="", flush=True)
            result = chatbot.get_response(user_input, user_id)
            
            print(result['response'])
            
            # Show additional info in debug mode
            if '--debug' in sys.argv:
                print(f"   [Intent: {result['intent']}, Confidence: {result['confidence']:.2f}, Sentiment: {result['sentiment']}]")
        
        except KeyboardInterrupt:
            print("\n\n👋 Chat ended. Goodbye!")
            break
        except Exception as e:
            print(f"\n❌ Error: {e}")
            print("Please try again or type 'quit' to exit.")

def print_help():
    """Print help information"""
    print("\n📚 Available Commands:")
    print("  help     - Show this help message")
    print("  quit     - Exit the chat")
    print("  exit     - Exit the chat")
    print("  bye      - Exit the chat")
    print("\n💡 Example Questions:")
    print("  - What courses do you offer?")
    print("  - Tell me about internships")
    print("  - What are the course fees?")
    print("  - How can I enroll?")
    print("  - Do you provide certificates?")
    print("\n🌐 Language Support:")
    print("  - English (default)")
    print("  - Hindi (हिंदी)")

if __name__ == "__main__":
    main()
