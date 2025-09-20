# SkillHigh AI Chatbot API Documentation

## Overview

The SkillHigh AI Chatbot provides a RESTful API for intelligent conversation with students about courses, fees, internships, and other SkillHigh-related queries.

## Base URL

```
http://localhost:5000
```

## Authentication

Currently, no authentication is required. For production deployment, consider implementing API keys or JWT tokens.

## Endpoints

### 1. Chat Endpoint

**POST** `/chat`

Main endpoint for interacting with the chatbot.

#### Request Body

```json
{
  "message": "string",
  "user_id": "string",
  "language": "string"
}
```

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `message` | string | Yes | User's message/query |
| `user_id` | string | No | Unique identifier for the user (default: "default") |
| `language` | string | No | Language code ("en" for English, "hi" for Hindi, default: "en") |

#### Response

```json
{
  "response": "string",
  "intent": "string",
  "confidence": "number",
  "sentiment": "string"
}
```

#### Response Fields

| Field | Type | Description |
|-------|------|-------------|
| `response` | string | Chatbot's response message |
| `intent` | string | Detected intent category |
| `confidence` | number | Confidence score (0.0 to 1.0) |
| `sentiment` | string | Sentiment analysis result ("positive", "negative", "neutral") |

#### Example Request

```bash
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{
    "message": "What courses do you offer?",
    "user_id": "student123",
    "language": "en"
  }'
```

#### Example Response

```json
{
  "response": "We offer comprehensive courses in Data Science, Web Development, AI/ML, Digital Marketing, and UI/UX Design. Each course includes hands-on projects, industry mentorship, and placement assistance. Would you like details about any specific course?",
  "intent": "AskCourses",
  "confidence": 0.85,
  "sentiment": "neutral"
}
```

### 2. Analytics Endpoint

**GET** `/analytics`

Retrieve usage analytics and statistics.

#### Response

```json
{
  "total_conversations": "number",
  "intent_counts": {
    "Greeting": "number",
    "AskCourses": "number",
    "AskFees": "number",
    "...": "number"
  },
  "sentiment_counts": {
    "positive": "number",
    "negative": "number",
    "neutral": "number"
  },
  "language_usage": {
    "en": "number",
    "hi": "number"
  },
  "daily_stats": {
    "date": "number"
  }
}
```

#### Example Request

```bash
curl -X GET http://localhost:5000/analytics
```

#### Example Response

```json
{
  "total_conversations": 150,
  "intent_counts": {
    "Greeting": 45,
    "AskCourses": 30,
    "AskFees": 25,
    "AskInternship": 20,
    "AskCertification": 15,
    "AskPlacement": 10,
    "AskDuration": 5
  },
  "sentiment_counts": {
    "positive": 80,
    "negative": 15,
    "neutral": 55
  },
  "language_usage": {
    "en": 120,
    "hi": 30
  },
  "daily_stats": {
    "2025-09-20": 25,
    "2025-09-19": 30,
    "2025-09-18": 20
  }
}
```

### 3. Health Check Endpoint

**GET** `/health`

Check the API server status.

#### Response

```json
{
  "status": "healthy",
  "timestamp": "string",
  "version": "string"
}
```

#### Example Request

```bash
curl -X GET http://localhost:5000/health
```

#### Example Response

```json
{
  "status": "healthy",
  "timestamp": "2025-09-20T22:00:00Z",
  "version": "1.0.0"
}
```

### 4. Session Management

#### Get Session History

**GET** `/session/<user_id>`

Retrieve conversation history for a specific user.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User identifier |

#### Response

```json
{
  "user_id": "string",
  "conversations": [
    {
      "intent": "string",
      "response": "string",
      "timestamp": "string"
    }
  ]
}
```

#### Example Request

```bash
curl -X GET http://localhost:5000/session/student123
```

#### Clear Session

**DELETE** `/session/<user_id>`

Clear conversation history for a specific user.

#### Parameters

| Parameter | Type | Required | Description |
|-----------|------|----------|-------------|
| `user_id` | string | Yes | User identifier |

#### Response

```json
{
  "message": "Session cleared successfully",
  "user_id": "string"
}
```

#### Example Request

```bash
curl -X DELETE http://localhost:5000/session/student123
```

## Intent Categories

The chatbot recognizes the following intent categories:

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

## Error Handling

### Error Response Format

```json
{
  "error": "string",
  "message": "string",
  "status_code": "number"
}
```

### Common Error Codes

| Status Code | Description |
|-------------|-------------|
| 400 | Bad Request - Invalid request format |
| 404 | Not Found - Endpoint not found |
| 500 | Internal Server Error - Server error |

### Example Error Response

```json
{
  "error": "Bad Request",
  "message": "Missing required field: message",
  "status_code": 400
}
```

## Rate Limiting

Currently, no rate limiting is implemented. For production deployment, consider implementing rate limiting to prevent abuse.

## CORS

Cross-Origin Resource Sharing (CORS) is enabled for all origins. For production, restrict CORS to specific domains.

## WebSocket Support

WebSocket support is not currently implemented. For real-time chat, consider implementing WebSocket endpoints.

## SDK Examples

### Python

```python
import requests

def chat_with_bot(message, user_id="default", language="en"):
    url = "http://localhost:5000/chat"
    data = {
        "message": message,
        "user_id": user_id,
        "language": language
    }
    response = requests.post(url, json=data)
    return response.json()

# Example usage
result = chat_with_bot("What courses do you offer?")
print(result["response"])
```

### JavaScript

```javascript
async function chatWithBot(message, userId = "default", language = "en") {
    const response = await fetch("http://localhost:5000/chat", {
        method: "POST",
        headers: {
            "Content-Type": "application/json",
        },
        body: JSON.stringify({
            message: message,
            user_id: userId,
            language: language
        })
    });
    return await response.json();
}

// Example usage
chatWithBot("What courses do you offer?")
    .then(result => console.log(result.response));
```

### cURL

```bash
# Basic chat
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hello", "user_id": "test", "language": "en"}'

# Get analytics
curl -X GET http://localhost:5000/analytics

# Health check
curl -X GET http://localhost:5000/health
```

## Testing

### Test the API

```bash
# Test chat endpoint
curl -X POST http://localhost:5000/chat \
  -H "Content-Type: application/json" \
  -d '{"message": "Hi", "user_id": "test", "language": "en"}'

# Test analytics
curl -X GET http://localhost:5000/analytics

# Test health check
curl -X GET http://localhost:5000/health
```

## Production Deployment

For production deployment:

1. **Environment Variables**
   - Set `FLASK_ENV=production`
   - Configure database connections
   - Set up logging

2. **Security**
   - Implement authentication
   - Add rate limiting
   - Enable HTTPS
   - Restrict CORS

3. **Monitoring**
   - Set up logging
   - Monitor API performance
   - Track error rates

4. **Scaling**
   - Use a production WSGI server (Gunicorn)
   - Implement load balancing
   - Use a reverse proxy (Nginx)

## Support

For API support and questions:
- Create an issue on GitHub
- Check the troubleshooting guide
- Review the documentation
