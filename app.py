from flask import Flask, render_template, request, jsonify
import time
import random
import re

app = Flask(__name__)

conversation_history = []

def chatbot_response(user_input):
    user_input = user_input.lower().strip()
    
    if any(word in user_input for word in ["hi", "hello", "hey", "good morning", "good afternoon", "good evening"]):
        greetings = [
            "Hi there! I'm your friendly chatbot assistant. How can I help you today?",
            "Hello! Great to see you here. What would you like to talk about?",
            "Hey! I'm here and ready to chat. What's on your mind?",
            "Hi! Welcome to our chat. How can I assist you today?"
        ]
        return random.choice(greetings)
    
    elif any(phrase in user_input for phrase in ["what is your name", "your name", "who are you"]):
        return "I'm ChatBot AI, your virtual assistant! I'm here to help answer your questions and have a friendly conversation."
    
    elif any(phrase in user_input for phrase in ["where are you from", "where do you live", "your location"]):
        return "I exist in the digital realm of servers and code! I'm always online and ready to help from anywhere in the world."
    
    elif any(phrase in user_input for phrase in ["how are you", "how do you feel", "what's up"]):
        responses = [
            "I'm doing great, thank you for asking! How are you doing today?",
            "I'm functioning perfectly and ready to help! How about you?",
            "I'm wonderful! Every conversation makes my day. How are you feeling?"
        ]
        return random.choice(responses)
    
    elif any(word in user_input for word in ["hobbies", "interests", "like to do", "enjoy"]):
        return "My favorite hobby is learning from conversations like ours! I love helping people, solving problems, and discovering new topics to discuss."
    
    elif any(phrase in user_input for phrase in ["what did you eat", "do you eat", "favorite food", "hungry"]):
        return "I don't eat food, but I feast on data and knowledge! I'd love to help you find recipes or discuss your favorite cuisines though."
    
    elif "color" in user_input:
        return "I appreciate all colors equally! But if I had to choose, I'd say blue - it reminds me of the digital world I inhabit."
    
    elif any(word in user_input for word in ["music", "song", "listen", "band", "artist"]):
        return "I can't listen to music, but I find the concept fascinating! Music is such a universal language. What kind of music do you enjoy?"
    
    elif any(phrase in user_input for phrase in ["joke", "funny", "make me laugh", "humor"]):
        jokes = [
            "Why did the scarecrow win an award? Because he was outstanding in his field!",
            "Why don't scientists trust atoms? Because they make up everything!",
            "What do you call a fake noodle? An impasta!",
            "Why did the math book look so sad? Because it had too many problems!",
            "What do you call a bear with no teeth? A gummy bear!"
        ]
        return random.choice(jokes)
    
    elif any(phrase in user_input for phrase in ["fact", "interesting", "tell me something", "did you know"]):
        facts = [
            "Did you know that honey never spoils? Archaeologists have found edible honey in ancient Egyptian tombs!",
            "Here's a fun fact: A group of flamingos is called a 'flamboyance'!",
            "Interesting fact: The shortest war in history lasted only 38-45 minutes between Britain and Zanzibar in 1896!",
            "Did you know that octopuses have three hearts and blue blood?",
            "Fun fact: Bananas are berries, but strawberries aren't!"
        ]
        return random.choice(facts)
    
    elif "weather" in user_input:
        return "I don't have access to real-time weather data, but I recommend checking a weather app or website for accurate forecasts!"
    
    elif any(word in user_input for word in ["news", "headlines", "current events"]):
        return "I don't have access to current news, but I'd suggest checking reliable news sources for the latest updates!"
    
    elif "translate" in user_input:
        return "I don't have translation capabilities built-in, but I can help you find good translation tools or discuss languages!"
    
    elif any(word in user_input for word in ["calculate", "math", "plus", "minus", "multiply", "divide"]):
        math_pattern = r'(\d+)\s*([\+\-\*\/])\s*(\d+)'
        match = re.search(math_pattern, user_input)
        if match:
            num1, operator, num2 = match.groups()
            try:
                num1, num2 = float(num1), float(num2)
                if operator == '+':
                    result = num1 + num2
                elif operator == '-':
                    result = num1 - num2
                elif operator == '*':
                    result = num1 * num2
                elif operator == '/':
                    if num2 != 0:
                        result = num1 / num2
                    else:
                        return "I can't divide by zero! That would break the universe! 🌌"
                return f"The answer is {result}! 🔢"
            except:
                return "I had trouble calculating that. Can you try rephrasing your math question?"
        else:
            return "I can help with simple math! Try asking something like '10 + 5' or 'what is 8 * 7?'"
    
    elif any(phrase in user_input for phrase in ["time", "what time", "current time"]):
        current_time = time.strftime("%I:%M %p on %B %d, %Y")
        return f"The current time is {current_time}. ⏰"
    
    elif any(word in user_input for word in ["help", "assist", "support", "what can you do"]):
        return """I can help you with various things:
        • Answer general questions
        • Tell jokes and share interesting facts
        • Have casual conversations
        • Provide the current time
        • Chat about topics like music, food, hobbies, and more!
        
        Just type your question or topic, and I'll do my best to help!"""
    
    elif any(phrase in user_input for phrase in ["how old", "your age", "age"]):
        return "I don't age like humans do! I was created recently, but I'm constantly learning and improving with each conversation."
    
    elif any(word in user_input for word in ["thank", "thanks", "appreciate", "awesome", "great", "amazing"]):
        return "You're very welcome! I'm happy I could help. Is there anything else you'd like to chat about?"
    
    elif any(word in user_input for word in ["bye", "goodbye", "see you", "farewell", "exit", "quit"]):
        farewells = [
            "Goodbye! It was wonderful chatting with you. Have a fantastic day!",
            "See you later! Feel free to come back anytime for another chat.",
            "Farewell! Thanks for the great conversation. Take care!",
            "Bye! Hope to chat with you again soon. Have a great day!"
        ]
        return random.choice(farewells)
    
    else:
        default_responses = [
            "I'm not sure I understand that completely. Could you rephrase your question?",
            "That's interesting! Can you tell me more about what you're looking for?",
            "I'm still learning! Could you ask that in a different way?",
            "Hmm, I'm not quite sure how to respond to that. What else would you like to know?",
            "I'd love to help! Can you provide a bit more context or ask in another way?"
        ]
        return random.choice(default_responses)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/chat', methods=['POST'])
def chat():
    user_message = request.json.get('message', '')
    if user_message:
        conversation_history.append({'user': user_message, 'timestamp': time.time()})
        
        bot_response = chatbot_response(user_message)
        
        conversation_history.append({'bot': bot_response, 'timestamp': time.time()})
        
        if len(conversation_history) > 50:
            conversation_history.pop(0)
        
        return jsonify({'response': bot_response})
    return jsonify({'response': 'Please enter a message!'})

if __name__ == '__main__':
    app.run(debug=True)