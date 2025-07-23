# 🤖 ChatBot AI - Your Virtual Assistant

A friendly and interactive chatbot application built with Flask and modern web technologies. This chatbot can engage in conversations, tell jokes, share interesting facts, perform basic calculations, and much more!

## ✨ Features

### 🗣️ Conversational Abilities
- **Smart Greetings**: Responds to various greeting patterns with friendly messages
- **Personal Questions**: Answers questions about itself and its capabilities
- **Casual Conversations**: Engages in topics like music, food, hobbies, and daily life
- **Helpful Responses**: Provides assistance and guidance when asked

### 🎯 Interactive Functions
- **🎭 Joke Telling**: Shares funny jokes to brighten your day
- **📚 Interesting Facts**: Provides fascinating facts about various topics
- **🧮 Basic Calculator**: Performs simple mathematical operations (+, -, *, /)
- **⏰ Time Display**: Shows current date and time
- **❓ Help System**: Explains available features and capabilities

### 🎨 Modern Web Interface
- **Responsive Design**: Works perfectly on desktop and mobile devices
- **Beautiful UI**: Modern gradient background with smooth animations
- **Real-time Chat**: Instant messaging with typing indicators
- **Message History**: Maintains conversation context
- **Auto-scroll**: Automatically scrolls to latest messages

## 🚀 Quick Start

### Prerequisites
- Python 3.7 or higher
- pip (Python package installer)

### Installation & Setup

#### Option 1: Automated Setup (Windows)
1. **Clone or download** this repository
2. **Run the setup script**:
   ```bash
   setup.bat
   ```
3. **Start the application**:
   ```bash
   run.bat
   ```

#### Option 2: Manual Setup
1. **Clone the repository**:
   ```bash
   git clone <your-repository-url>
   cd Task-1-Chatbot
   ```

2. **Create a virtual environment**:
   ```bash
   python -m venv chatbot_env
   ```

3. **Activate the virtual environment**:
   - **Windows**:
     ```bash
     chatbot_env\Scripts\activate
     ```
   - **macOS/Linux**:
     ```bash
     source chatbot_env/bin/activate
     ```

4. **Install dependencies**:
   ```bash
   pip install -r requirements.txt
   ```

5. **Run the application**:
   ```bash
   python app.py
   ```

6. **Open your browser** and navigate to:
   ```
   http://127.0.0.1:5000
   ```

## 📁 Project Structure

```
Task-1-Chatbot/
├── app.py              # Main Flask application
├── Code.py             # Alternative console-based chatbot
├── requirements.txt    # Python dependencies
├── setup.bat          # Automated setup script (Windows)
├── run.bat            # Quick run script (Windows)
├── templates/
│   └── index.html     # Web interface template
└── README.md          # Project documentation
```

## 🛠️ Technical Details

### Backend (Flask)
- **Framework**: Flask 2.3.2
- **Language**: Python 3.x
- **Features**:
  - RESTful API endpoints
  - JSON response handling
  - Conversation history management
  - Pattern matching for user inputs

### Frontend (HTML/CSS/JavaScript)
- **Responsive Design**: Mobile-first approach
- **Modern CSS**: Flexbox layout with gradient backgrounds
- **Interactive JavaScript**: Real-time messaging and animations
- **User Experience**: Typing indicators and smooth transitions

### Dependencies
- `Flask==2.3.2` - Web framework
- `Werkzeug==2.3.6` - WSGI utility library
- `Jinja2==3.1.2` - Template engine
- `MarkupSafe==2.1.3` - String handling
- `itsdangerous==2.1.2` - Data signing
- `click==8.x` - Command line interface

## 💬 How to Use

### Starting a Conversation
1. Open the web interface in your browser
2. Type your message in the input field
3. Press Enter or click the "Send" button
4. Watch the chatbot respond with helpful and engaging replies!

### Example Interactions

**Greetings:**
- "Hi there!"
- "Hello, how are you?"
- "Good morning!"

**Questions:**
- "What's your name?"
- "Tell me a joke"
- "What's an interesting fact?"
- "What time is it?"

**Math Operations:**
- "Calculate 15 + 25"
- "What is 8 * 7?"
- "10 / 2"

**General Chat:**
- "Do you like music?"
- "What are your hobbies?"
- "Tell me about yourself"

## 🎯 Chatbot Capabilities

### Smart Response System
The chatbot uses pattern matching to understand user inputs and provides contextually appropriate responses:

- **Greeting Detection**: Recognizes various greeting patterns
- **Question Classification**: Identifies different types of questions
- **Math Processing**: Parses and calculates mathematical expressions
- **Fallback Responses**: Provides helpful responses for unrecognized inputs

### Conversation Features
- **Memory**: Maintains conversation history (last 50 exchanges)
- **Randomization**: Varies responses to keep conversations fresh
- **Error Handling**: Gracefully handles unexpected inputs
- **Time Awareness**: Provides current date and time information

## 🔧 Customization

### Adding New Responses
To add new chatbot responses, edit the `chatbot_response()` function in `app.py`:

```python
elif "your_keyword" in user_input:
    return "Your custom response here!"
```

### Modifying the Interface
- **Styling**: Edit the CSS in `templates/index.html`
- **Layout**: Modify the HTML structure
- **Behavior**: Update the JavaScript functions

### Configuration
- **Port**: Change the port in `app.py` (default: 5000)
- **Debug Mode**: Toggle debug mode in the Flask app configuration
- **History Limit**: Adjust conversation history limit (default: 50 messages)

## 🚀 Deployment

### Local Development
The application runs in debug mode by default for development purposes.

### Production Deployment
For production deployment, consider:
- Setting `debug=False` in `app.py`
- Using a production WSGI server like Gunicorn
- Implementing proper error logging
- Adding security headers and HTTPS

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request


## 🆘 Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
# Kill the process using port 5000
netstat -ano | findstr :5000
taskkill /PID <process_id> /F
```

**Module Not Found:**
```bash
# Ensure virtual environment is activated
pip install -r requirements.txt
```

**Browser Not Opening:**
- Manually navigate to `http://127.0.0.1:5000`
- Check if the Flask server is running
- Verify no firewall is blocking the connection

## 📞 Support

If you encounter any issues or have questions:
1. Check the troubleshooting section above
2. Review the console output for error messages
3. Ensure all dependencies are properly installed
4. Verify Python version compatibility

## 🎉 Acknowledgments

- Built as part of CodSoft internship program
- Inspired by modern chatbot interfaces
- Uses Flask framework for robust web development

---

**Happy Chatting! 🎊**

*Made with ❤️ for interactive conversations*
