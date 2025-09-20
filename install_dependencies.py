# Installation script for SkillHigh Chatbot dependencies

import subprocess
import sys
import os

def install_package(package):
    """Install a package using pip"""
    try:
        subprocess.check_call([sys.executable, "-m", "pip", "install", package])
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Failed to install {package}: {e}")
        return False

def main():
    """Main installation function"""
    print("🤖 SkillHigh Chatbot - Dependency Installer")
    print("=" * 50)
    
    # Core packages (install in order to avoid conflicts)
    packages = [
        "numpy==1.24.3",
        "pandas==2.1.3",
        "scikit-learn==1.3.2",
        "nltk==3.8.1",
        "textblob==0.17.1",
        "flask==2.3.3",
        "flask-cors==4.0.0",
        "streamlit==1.28.1",
        "plotly==5.17.0",
        "requests>=2.25.0",
        "httpx>=0.23.0,<1.0.0",
        "googletrans==4.0.0rc1",
        "python-dotenv==1.0.0",
        "spacy==3.7.2",
        "transformers==4.35.2",
        "torch==2.1.1",
        "sentence-transformers==2.2.2"
    ]
    
    print("📦 Installing dependencies...")
    print()
    
    failed_packages = []
    
    for package in packages:
        print(f"Installing {package}...")
        if install_package(package):
            print(f"✅ {package} installed successfully")
        else:
            print(f"❌ {package} installation failed")
            failed_packages.append(package)
        print()
    
    # Download NLTK data
    print("📚 Downloading NLTK data...")
    try:
        import nltk
        nltk.download('punkt', quiet=True)
        nltk.download('stopwords', quiet=True)
        nltk.download('wordnet', quiet=True)
        print("✅ NLTK data downloaded successfully")
    except Exception as e:
        print(f"❌ Failed to download NLTK data: {e}")
    
    print()
    print("=" * 50)
    
    if failed_packages:
        print("⚠️ Some packages failed to install:")
        for package in failed_packages:
            print(f"   - {package}")
        print("\nYou can try installing them manually:")
        for package in failed_packages:
            print(f"   pip install {package}")
    else:
        print("🎉 All dependencies installed successfully!")
        print("\nYou can now run the chatbot:")
        print("   python app/api.py          # Start API server")
        print("   streamlit run demo_app.py  # Start demo app")
        print("   python cli_chat.py         # Command line interface")

if __name__ == "__main__":
    main()
