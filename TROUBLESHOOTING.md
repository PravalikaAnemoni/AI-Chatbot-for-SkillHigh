# 🔧 Troubleshooting Guide - SkillHigh Chatbot

## 🚨 Common Installation Issues

### 1. Dependency Conflicts (httpx, openai, etc.)

**Problem**: Version conflicts between packages
```
ERROR: pip's dependency resolver does not currently take into account all the packages that are installed. This behaviour is the source of the following dependency conflicts.
openai 1.3.7 requires httpx<1,>=0.23.0, but you have httpx 0.13.3 which is incompatible.
```

**Solutions**:

#### Option A: Use the installation script
```bash
python install_dependencies.py
```

#### Option B: Manual installation with conflict resolution
```bash
# Upgrade pip first
python -m pip install --upgrade pip

# Install with specific versions
pip install httpx>=0.23.0,<1.0.0
pip install requests>=2.25.0

# Then install other packages
pip install -r requirements.txt
```

#### Option C: Create a virtual environment (Recommended)
```bash
# Create virtual environment
python -m venv skillhigh_chatbot_env

# Activate virtual environment
# On Windows:
skillhigh_chatbot_env\Scripts\activate
# On macOS/Linux:
source skillhigh_chatbot_env/bin/activate

# Install packages
pip install -r requirements.txt
```

### 2. NLTK Data Not Found

**Problem**: NLTK corpora not downloaded
```
LookupError: Resource punkt not found
```

**Solution**:
```python
import nltk
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('wordnet')
```

Or run the installation script which handles this automatically.

### 3. Google Translate API Issues

**Problem**: Translation not working
```
Error: Translation failed
```

**Solutions**:
- Check internet connection
- The chatbot will fallback to English if translation fails
- Translation is optional - the chatbot works without it

### 4. Port Already in Use

**Problem**: API server can't start
```
OSError: [Errno 48] Address already in use
```

**Solutions**:
```bash
# Find process using port 5000
netstat -ano | findstr :5000

# Kill the process (Windows)
taskkill /PID <process_id> /F

# Or use a different port
python app/api.py --port 5001
```

### 5. Streamlit Issues

**Problem**: Streamlit app won't start
```
ModuleNotFoundError: No module named 'streamlit'
```

**Solution**:
```bash
pip install streamlit
streamlit run demo_app.py
```

## 🐛 Runtime Issues

### 1. API Connection Error

**Problem**: Demo app can't connect to API
```
ConnectionError: Failed to connect to API server
```

**Solutions**:
1. Make sure API server is running: `python app/api.py`
2. Check if port 5000 is accessible
3. Verify API URL in demo app settings
4. Check firewall settings

### 2. Model Training Errors

**Problem**: Chatbot fails to initialize
```
Error training model: File not found
```

**Solutions**:
1. Ensure `data/intents.csv` exists
2. Check file permissions
3. Verify CSV format (Text,Intent,Response columns)

### 3. Memory Issues

**Problem**: Out of memory errors
```
MemoryError: Unable to allocate array
```

**Solutions**:
1. Close other applications
2. Reduce batch size in model training
3. Use smaller TF-IDF features: `max_features=500`

## 🔍 Debug Mode

### Enable Debug Logging
```bash
# Set environment variable
export FLASK_DEBUG=1

# Run API with debug
python app/api.py
```

### Test Individual Components
```bash
# Test chatbot core
python test_chatbot.py

# Test API endpoints
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi", "user_id": "test", "language": "en"}'
```

## 🛠️ System Requirements

### Minimum Requirements
- Python 3.8+
- 4GB RAM
- 2GB free disk space
- Internet connection (for translation)

### Recommended Requirements
- Python 3.9+
- 8GB RAM
- 5GB free disk space
- Stable internet connection

## 📞 Getting Help

### 1. Check Logs
```bash
# API server logs
python app/api.py 2>&1 | tee api.log

# Streamlit logs
streamlit run demo_app.py 2>&1 | tee streamlit.log
```

### 2. Verify Installation
```python
# Test imports
try:
    import flask
    import streamlit
    import sklearn
    import nltk
    import pandas
    print("✅ All core packages imported successfully")
except ImportError as e:
    print(f"❌ Import error: {e}")
```

### 3. Test Basic Functionality
```python
# Quick test
from app.chatbot import initialize_chatbot, get_chatbot

# Initialize
success = initialize_chatbot()
print(f"Initialization: {'✅ Success' if success else '❌ Failed'}")

# Test response
if success:
    chatbot = get_chatbot()
    result = chatbot.get_response("Hi")
    print(f"Test response: {result['response']}")
```

## 🔄 Reset and Reinstall

### Complete Reset
```bash
# Remove virtual environment
rm -rf skillhigh_chatbot_env

# Clear pip cache
pip cache purge

# Reinstall everything
python install_dependencies.py
```

### Partial Reset
```bash
# Uninstall problematic packages
pip uninstall httpx openai -y

# Reinstall with correct versions
pip install httpx>=0.23.0,<1.0.0
```

## 📋 Pre-flight Checklist

Before running the chatbot, ensure:

- [ ] Python 3.8+ installed
- [ ] All dependencies installed successfully
- [ ] NLTK data downloaded
- [ ] `data/intents.csv` exists and is readable
- [ ] Port 5000 is available
- [ ] Internet connection (for translation)
- [ ] Sufficient disk space and memory

## 🎯 Quick Fixes

### Most Common Issues and Solutions

1. **"Module not found"** → Run `pip install -r requirements.txt`
2. **"Port in use"** → Kill process or use different port
3. **"NLTK data missing"** → Run `python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"`
4. **"Translation failed"** → Check internet connection (optional feature)
5. **"API connection error"** → Ensure API server is running on port 5000

---

**Still having issues?** Check the logs, verify your installation, and ensure all system requirements are met. The chatbot is designed to be robust and handle most errors gracefully.
