# Deployment Guide - SkillHigh AI Chatbot

This guide provides step-by-step instructions for deploying the SkillHigh AI Chatbot in various environments.

## 🚀 Quick Start

### Local Development

1. **Clone the repository**
   ```bash
   git clone https://github.com/your-username/skillhigh_chatbot.git
   cd skillhigh_chatbot
   ```

2. **Set up virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   python install_dependencies.py
   ```

4. **Run the application**
   ```bash
   # Start API server
   python run_api.py
   
   # In another terminal, start demo app
   streamlit run demo_app.py
   ```

## 🌐 Production Deployment

### Option 1: Docker Deployment

#### 1. Create Dockerfile

```dockerfile
FROM python:3.9-slim

WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    gcc \
    g++ \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements and install Python dependencies
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copy application code
COPY . .

# Download NLTK data
RUN python -c "import nltk; nltk.download('punkt'); nltk.download('stopwords'); nltk.download('wordnet')"

# Expose port
EXPOSE 5000

# Run the application
CMD ["python", "run_api.py"]
```

#### 2. Create docker-compose.yml

```yaml
version: '3.8'

services:
  chatbot-api:
    build: .
    ports:
      - "5000:5000"
    environment:
      - FLASK_ENV=production
    volumes:
      - ./data:/app/data
    restart: unless-stopped

  chatbot-demo:
    build: .
    ports:
      - "8501:8501"
    command: streamlit run demo_app.py --server.port=8501 --server.address=0.0.0.0
    environment:
      - FLASK_ENV=production
    depends_on:
      - chatbot-api
    restart: unless-stopped
```

#### 3. Deploy with Docker

```bash
# Build and run
docker-compose up -d

# Check status
docker-compose ps

# View logs
docker-compose logs -f
```

### Option 2: Cloud Deployment

#### Heroku Deployment

1. **Create Procfile**
   ```
   web: gunicorn app.api:app
   ```

2. **Create runtime.txt**
   ```
   python-3.9.18
   ```

3. **Deploy to Heroku**
   ```bash
   # Install Heroku CLI
   # Login to Heroku
   heroku login
   
   # Create app
   heroku create skillhigh-chatbot
   
   # Deploy
   git push heroku main
   
   # Open app
   heroku open
   ```

#### AWS EC2 Deployment

1. **Launch EC2 Instance**
   - Choose Ubuntu 20.04 LTS
   - Select t2.micro (free tier)
   - Configure security groups (ports 22, 80, 443, 5000, 8501)

2. **Connect and Setup**
   ```bash
   # Connect via SSH
   ssh -i your-key.pem ubuntu@your-ec2-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python and pip
   sudo apt install python3 python3-pip python3-venv -y
   
   # Install Nginx
   sudo apt install nginx -y
   ```

3. **Deploy Application**
   ```bash
   # Clone repository
   git clone https://github.com/your-username/skillhigh_chatbot.git
   cd skillhigh_chatbot
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   python install_dependencies.py
   
   # Install Gunicorn
   pip install gunicorn
   ```

4. **Configure Nginx**
   ```bash
   # Create Nginx configuration
   sudo nano /etc/nginx/sites-available/skillhigh-chatbot
   ```

   ```nginx
   server {
       listen 80;
       server_name your-domain.com;
       
       location / {
           proxy_pass http://127.0.0.1:5000;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
       
       location /demo {
           proxy_pass http://127.0.0.1:8501;
           proxy_set_header Host $host;
           proxy_set_header X-Real-IP $remote_addr;
           proxy_set_header X-Forwarded-For $proxy_add_x_forwarded_for;
           proxy_set_header X-Forwarded-Proto $scheme;
       }
   }
   ```

   ```bash
   # Enable site
   sudo ln -s /etc/nginx/sites-available/skillhigh-chatbot /etc/nginx/sites-enabled/
   sudo nginx -t
   sudo systemctl restart nginx
   ```

5. **Create Systemd Service**
   ```bash
   sudo nano /etc/systemd/system/skillhigh-chatbot.service
   ```

   ```ini
   [Unit]
   Description=SkillHigh Chatbot API
   After=network.target
   
   [Service]
   User=ubuntu
   Group=ubuntu
   WorkingDirectory=/home/ubuntu/skillhigh_chatbot
   Environment="PATH=/home/ubuntu/skillhigh_chatbot/venv/bin"
   ExecStart=/home/ubuntu/skillhigh_chatbot/venv/bin/gunicorn --workers 3 --bind 0.0.0.0:5000 app.api:app
   
   [Install]
   WantedBy=multi-user.target
   ```

   ```bash
   # Start service
   sudo systemctl daemon-reload
   sudo systemctl start skillhigh-chatbot
   sudo systemctl enable skillhigh-chatbot
   ```

#### Google Cloud Platform (GCP)

1. **Create App Engine Configuration**
   ```yaml
   # app.yaml
   runtime: python39
   
   env_variables:
     FLASK_ENV: production
   
   handlers:
   - url: /.*
     script: auto
   ```

2. **Deploy to App Engine**
   ```bash
   # Install Google Cloud SDK
   # Initialize project
   gcloud init
   
   # Deploy
   gcloud app deploy
   ```

### Option 3: VPS Deployment

#### DigitalOcean Droplet

1. **Create Droplet**
   - Choose Ubuntu 20.04
   - Select appropriate size
   - Add SSH keys

2. **Setup Application**
   ```bash
   # Connect via SSH
   ssh root@your-droplet-ip
   
   # Create user
   adduser skillhigh
   usermod -aG sudo skillhigh
   
   # Switch to user
   su - skillhigh
   
   # Install dependencies
   sudo apt update
   sudo apt install python3 python3-pip python3-venv nginx -y
   
   # Clone and setup app
   git clone https://github.com/your-username/skillhigh_chatbot.git
   cd skillhigh_chatbot
   python3 -m venv venv
   source venv/bin/activate
   pip install -r requirements.txt
   pip install gunicorn
   python install_dependencies.py
   ```

3. **Configure and Start**
   ```bash
   # Create systemd service (similar to AWS setup)
   # Configure Nginx (similar to AWS setup)
   # Start services
   ```

## 🔧 Configuration

### Environment Variables

Create a `.env` file for production:

```env
FLASK_ENV=production
FLASK_DEBUG=False
SECRET_KEY=your-secret-key-here
DATABASE_URL=your-database-url
REDIS_URL=your-redis-url
```

### Production Settings

Update `app/api.py` for production:

```python
if __name__ == '__main__':
    app.run(
        host='0.0.0.0',
        port=int(os.environ.get('PORT', 5000)),
        debug=False
    )
```

## 📊 Monitoring and Logging

### Logging Configuration

```python
import logging
from logging.handlers import RotatingFileHandler

if not app.debug:
    file_handler = RotatingFileHandler('logs/skillhigh_chatbot.log', maxBytes=10240, backupCount=10)
    file_handler.setFormatter(logging.Formatter(
        '%(asctime)s %(levelname)s: %(message)s [in %(pathname)s:%(lineno)d]'
    ))
    file_handler.setLevel(logging.INFO)
    app.logger.addHandler(file_handler)
    app.logger.setLevel(logging.INFO)
    app.logger.info('SkillHigh Chatbot startup')
```

### Health Monitoring

```python
@app.route('/health')
def health_check():
    return jsonify({
        'status': 'healthy',
        'timestamp': datetime.utcnow().isoformat(),
        'version': '1.0.0',
        'uptime': time.time() - start_time
    })
```

## 🔒 Security Considerations

### 1. HTTPS Configuration

```nginx
server {
    listen 443 ssl;
    server_name your-domain.com;
    
    ssl_certificate /path/to/certificate.crt;
    ssl_certificate_key /path/to/private.key;
    
    # Security headers
    add_header X-Frame-Options DENY;
    add_header X-Content-Type-Options nosniff;
    add_header X-XSS-Protection "1; mode=block";
    
    location / {
        proxy_pass http://127.0.0.1:5000;
        # ... proxy settings
    }
}
```

### 2. Rate Limiting

```python
from flask_limiter import Limiter
from flask_limiter.util import get_remote_address

limiter = Limiter(
    app,
    key_func=get_remote_address,
    default_limits=["200 per day", "50 per hour"]
)

@app.route('/chat', methods=['POST'])
@limiter.limit("10 per minute")
def chat():
    # ... existing code
```

### 3. Input Validation

```python
from flask_wtf import FlaskForm
from wtforms import StringField, validators

class ChatForm(FlaskForm):
    message = StringField('Message', [validators.Length(min=1, max=1000)])
    user_id = StringField('User ID', [validators.Length(min=1, max=100)])
    language = StringField('Language', [validators.Length(min=2, max=5)])
```

## 📈 Performance Optimization

### 1. Caching

```python
from flask_caching import Cache

cache = Cache(app, config={'CACHE_TYPE': 'simple'})

@cache.memoize(timeout=300)
def get_chatbot_response(message, user_id, language):
    # ... existing code
```

### 2. Database Connection Pooling

```python
from sqlalchemy import create_engine
from sqlalchemy.pool import QueuePool

engine = create_engine(
    DATABASE_URL,
    poolclass=QueuePool,
    pool_size=10,
    max_overflow=20
)
```

### 3. Load Balancing

```nginx
upstream chatbot_backend {
    server 127.0.0.1:5000;
    server 127.0.0.1:5001;
    server 127.0.0.1:5002;
}

server {
    location / {
        proxy_pass http://chatbot_backend;
    }
}
```

## 🚨 Troubleshooting

### Common Issues

1. **Port Already in Use**
   ```bash
   # Find process using port
   lsof -i :5000
   
   # Kill process
   kill -9 PID
   ```

2. **Permission Denied**
   ```bash
   # Fix permissions
   chmod +x run_api.py
   chown -R user:user /path/to/app
   ```

3. **Module Not Found**
   ```bash
   # Check virtual environment
   which python
   pip list
   
   # Reinstall dependencies
   pip install -r requirements.txt
   ```

### Log Analysis

```bash
# View application logs
tail -f logs/skillhigh_chatbot.log

# View system logs
journalctl -u skillhigh-chatbot -f

# View Nginx logs
tail -f /var/log/nginx/error.log
```

## 📋 Deployment Checklist

- [ ] Code tested locally
- [ ] Dependencies installed
- [ ] Environment variables configured
- [ ] Database configured (if applicable)
- [ ] SSL certificate installed
- [ ] Firewall configured
- [ ] Monitoring setup
- [ ] Backup strategy implemented
- [ ] Documentation updated
- [ ] Performance tested

## 🔄 Updates and Maintenance

### Rolling Updates

```bash
# Pull latest changes
git pull origin main

# Restart services
sudo systemctl restart skillhigh-chatbot
sudo systemctl restart nginx
```

### Backup Strategy

```bash
# Backup application
tar -czf backup-$(date +%Y%m%d).tar.gz /path/to/app

# Backup database (if applicable)
pg_dump database_name > backup-$(date +%Y%m%d).sql
```

## 📞 Support

For deployment issues:
- Check logs for error messages
- Verify configuration files
- Test individual components
- Contact system administrator
- Create GitHub issue with deployment details
