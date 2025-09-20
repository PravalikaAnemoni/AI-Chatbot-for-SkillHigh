# 🤖 SkillHigh AI Chatbot

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Flask](https://img.shields.io/badge/Flask-2.0+-green.svg)](https://flask.palletsprojects.com)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.0+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-yellow.svg)](LICENSE)
[![Contributions Welcome](https://img.shields.io/badge/Contributions-Welcome-brightgreen.svg)](CONTRIBUTING.md)

An intelligent AI-powered chatbot for SkillHigh that assists students with course information, fees, internships, and onboarding support. Built with advanced NLP techniques and featuring a beautiful web interface.

## ✨ Features

### 🧠 **Core AI Capabilities**
- **NLP-based Intent Recognition**: TF-IDF vectorization + Multinomial Naive Bayes classifier
- **Contextual Memory**: Remembers conversation history for personalized responses
- **Sentiment Analysis**: Analyzes user emotions for empathetic interactions
- **Multilingual Support**: English and Hindi language support with real-time translation

### 🎯 **Student Support Features**
- **Course Information**: Comprehensive details about all SkillHigh programs
- **Fee Structure**: Transparent pricing and payment options
- **Internship Guidance**: Information about placement opportunities
- **Certification Details**: Industry-recognized certification information
- **Enrollment Support**: Step-by-step application guidance

### 📊 **Analytics & Monitoring**
- **Real-time Analytics**: Usage statistics and conversation insights
- **Intent Distribution**: Visual charts of user query patterns
- **Sentiment Tracking**: Emotional tone analysis over time
- **Language Usage**: Multilingual interaction statistics

### 🔌 **Integration Ready**
- **REST API**: Complete API for website and LMS integration
- **Web Interface**: Beautiful Streamlit demo application
- **Session Management**: User-specific conversation tracking
- **Health Monitoring**: System status and performance metrics

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- pip package manager
- Git

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/skillhigh_chatbot.git
   cd skillhigh_chatbot
   ```

2. **Create virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python install_dependencies.py
   ```

### Running the Application

1. **Start the API server**
   ```bash
   python run_api.py
   ```

2. **Start the demo app** (in a new terminal)
   ```bash
   streamlit run demo_app.py
   ```

3. **Access the application**
   - 🌐 **API**: http://localhost:5000
   - 🎨 **Demo App**: http://localhost:8501

## 📖 Usage Examples

### API Usage

**Chat with the bot**
```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "What courses do you offer?", "user_id": "student123", "language": "en"}'
```

**Get analytics**
```bash
curl -X GET http://localhost:5000/analytics
```

**Health check**
```bash
curl -X GET http://localhost:5000/health
```

### Python SDK Example

```python
import requests

def chat_with_skillhigh(message, user_id="default", language="en"):
    url = "http://localhost:5000/chat"
    data = {
        "message": message,
        "user_id": user_id,
        "language": language
    }
    response = requests.post(url, json=data)
    return response.json()

# Example usage
result = chat_with_skillhigh("What courses do you offer?")
print(result["response"])
```

## 🏗️ Project Structure

```
skillhigh_chatbot/
├── 📁 app/
│   ├── __init__.py
│   ├── api.py              # Flask REST API server
│   └── chatbot.py          # Core AI chatbot logic
├── 📁 data/
│   └── intents.csv         # Training data for intent recognition
├── 📁 models/              # Auto-generated trained models
├── 📄 demo_app.py          # Streamlit web interface
├── 📄 run_api.py           # API server launcher
├── 📄 cli_chat.py          # Command-line interface
├── 📄 test_chatbot.py      # Testing script
├── 📄 requirements.txt     # Python dependencies
├── 📄 install_dependencies.py  # Dependency installer
├── 📄 README.md            # This file
├── 📄 API_DOCUMENTATION.md # Complete API reference
├── 📄 DEPLOYMENT_GUIDE.md  # Production deployment guide
├── 📄 CONTRIBUTING.md      # Contribution guidelines
├── 📄 TROUBLESHOOTING.md   # Common issues and solutions
└── 📄 LICENSE              # MIT License
```

## 🎯 Intent Categories

The chatbot recognizes **16 different intent categories**:

| Intent | Description | Example Queries |
|--------|-------------|-----------------|
| `Greeting` | Greeting messages | "Hi", "Hello", "Good morning" |
| `AskCourses` | Course information | "What courses do you offer?", "Tell me about your programs" |
| `AskFees` | Fee-related queries | "How much do courses cost?", "What are the fees?" |
| `AskInternship` | Internship information | "Do you provide internships?", "Tell me about internships" |
| `AskCertification` | Certification queries | "Will I get a certificate?", "What about certifications?" |
| `AskPlacement` | Placement assistance | "Do you help with job placement?", "What about placements?" |
| `AskDuration` | Course duration | "How long are the courses?", "What is the duration?" |
| `AskMode` | Class format | "Are classes online or offline?", "What is the class format?" |
| `AskEnrollment` | Enrollment process | "How can I enroll?", "How do I apply?" |
| `AskPrerequisites` | Prerequisites | "What are the prerequisites?", "Do I need prior experience?" |
| `AskAbout` | About SkillHigh | "What is SkillHigh?", "Tell me about SkillHigh" |
| `AskCapabilities` | Bot capabilities | "What can you help me with?", "How can you help me?" |
| `AskHelp` | Help requests | "I need help", "I'm confused" |
| `AskRefund` | Refund policy | "Can I get a refund?", "What is your refund policy?" |
| `Gratitude` | Thank you messages | "Thanks!", "Thank you" |
| `Goodbye` | Farewell messages | "Bye", "Goodbye" |

## 🔌 API Endpoints

| Endpoint | Method | Description | Parameters |
|----------|--------|-------------|------------|
| `/chat` | POST | Main chat endpoint | `message`, `user_id`, `language` |
| `/analytics` | GET | Usage analytics | None |
| `/health` | GET | Health check | None |
| `/session/<user_id>` | GET | Get session history | `user_id` |
| `/session/<user_id>` | DELETE | Clear session | `user_id` |

## 📊 Performance Metrics

- **Response Time**: < 2 seconds average
- **Intent Classification Accuracy**: ~85-90%
- **Supported Languages**: English + Hindi
- **Session Memory**: 5 interactions per user
- **Training Data**: 40+ examples across 16 intent categories

## 🛠️ Configuration

### Environment Variables
```bash
FLASK_ENV=production          # Set to 'production' for deployment
PORT=5000                    # API server port
SECRET_KEY=your-secret-key   # Flask secret key
```

### Training Data
Edit `data/intents.csv` to add new training examples or modify responses:

```csv
Text,Intent,Response
"What courses do you offer?","AskCourses","We offer comprehensive courses in Data Science, Web Development, AI/ML, Digital Marketing, and UI/UX Design..."
```

## 🚀 Deployment

### Docker Deployment
```bash
# Build and run with Docker Compose
docker-compose up -d
```

### Cloud Deployment
- **Heroku**: See [DEPLOYMENT_GUIDE.md](DEPLOYMENT_GUIDE.md)
- **AWS EC2**: Complete setup instructions included
- **Google Cloud**: App Engine configuration provided

### Production Considerations
- Enable HTTPS with SSL certificates
- Implement rate limiting and authentication
- Set up monitoring and logging
- Configure load balancing for high traffic

## 🧪 Testing

### Run Tests
```bash
# Test chatbot functionality
python test_chatbot.py

# Test API endpoints
curl -X GET http://localhost:5000/health
curl -X POST http://localhost:5000/chat -H "Content-Type: application/json" -d '{"message": "Hi"}'
```

### Test Coverage
- Intent recognition accuracy
- Multilingual support
- Session memory functionality
- API endpoint responses
- Error handling

## 🐛 Troubleshooting

### Common Issues

1. **Import Errors**
   ```bash
   # Ensure you're in the project directory
   cd skillhigh_chatbot
   
   # Check Python path
   python -c "import sys; print(sys.path)"
   ```

2. **API Not Responding**
   ```bash
   # Check if API is running
   curl http://localhost:5000/health
   
   # Restart API server
   python run_api.py
   ```

3. **Streamlit Issues**
   ```bash
   # Clear Streamlit cache
   streamlit cache clear
   
   # Restart Streamlit
   streamlit run demo_app.py
   ```

For more troubleshooting help, see [TROUBLESHOOTING.md](TROUBLESHOOTING.md).

## 🤝 Contributing

We welcome contributions! Please see our [Contributing Guidelines](CONTRIBUTING.md) for details.

### How to Contribute
1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

### Areas for Contribution
- 🧠 Improve AI model accuracy
- 🌍 Add more language support
- 🎨 Enhance UI/UX design
- 📊 Add more analytics features
- 🧪 Write comprehensive tests
- 📚 Improve documentation

## 📄 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **NLTK** for natural language processing
- **scikit-learn** for machine learning algorithms
- **Flask** for the REST API framework
- **Streamlit** for the web interface
- **TextBlob** for sentiment analysis
- **Google Translate** for multilingual support

## 📞 Support

- 📧 **Email**: support@skillhigh.com
- 🐛 **Issues**: [GitHub Issues](https://github.com/your-username/skillhigh_chatbot/issues)
- 📖 **Documentation**: [API Documentation](API_DOCUMENTATION.md)
- 🚀 **Deployment**: [Deployment Guide](DEPLOYMENT_GUIDE.md)

## 🌟 Star History

[![Star History Chart](https://api.star-history.com/svg?repos=your-username/skillhigh_chatbot&type=Date)](https://star-history.com/#your-username/skillhigh_chatbot&Date)

---

<div align="center">

**Made with ❤️ for SkillHigh Students**

[⭐ Star this repo](https://github.com/your-username/skillhigh_chatbot) | [🐛 Report Bug](https://github.com/your-username/skillhigh_chatbot/issues) | [💡 Request Feature](https://github.com/your-username/skillhigh_chatbot/issues)

</div>