# Startup script for SkillHigh Chatbot Demo

import subprocess
import sys
import time
import threading
import webbrowser
from pathlib import Path

def run_api_server():
    """Run the Flask API server"""
    print("🚀 Starting API server...")
    try:
        subprocess.run([sys.executable, "app/api.py"], check=True)
    except KeyboardInterrupt:
        print("\n⏹️ API server stopped")
    except Exception as e:
        print(f"❌ Error running API server: {e}")

def run_streamlit_app():
    """Run the Streamlit demo app"""
    print("🎨 Starting Streamlit demo...")
    try:
        subprocess.run([sys.executable, "-m", "streamlit", "run", "demo_app.py"], check=True)
    except KeyboardInterrupt:
        print("\n⏹️ Streamlit app stopped")
    except Exception as e:
        print(f"❌ Error running Streamlit app: {e}")

def main():
    """Main function to start both services"""
    print("🤖 SkillHigh AI Chatbot Demo")
    print("=" * 40)
    print()
    
    # Check if required files exist
    required_files = ["app/api.py", "app/chatbot.py", "demo_app.py", "data/intents.csv"]
    missing_files = [f for f in required_files if not Path(f).exists()]
    
    if missing_files:
        print("❌ Missing required files:")
        for file in missing_files:
            print(f"   - {file}")
        print("\nPlease ensure all files are present before running the demo.")
        return
    
    print("✅ All required files found!")
    print()
    
    # Start API server in a separate thread
    api_thread = threading.Thread(target=run_api_server, daemon=True)
    api_thread.start()
    
    # Wait a moment for API to start
    print("⏳ Waiting for API server to start...")
    time.sleep(3)
    
    # Start Streamlit app
    print("🌐 Opening demo in browser...")
    time.sleep(2)
    
    try:
        run_streamlit_app()
    except KeyboardInterrupt:
        print("\n👋 Demo stopped. Thank you for trying SkillHigh Chatbot!")

if __name__ == "__main__":
    main()
