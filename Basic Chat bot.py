print("🤖 ChatBot: Hello! I'm your mini chatbot. Type something to begin (type 'bye' to exit).")

responses = {
    "hi": "Hello!",
     "hello": "Hi there! 👋",
    "how are you": "I'm just code, but I'm feeling great! 💻",
    "what is your name": "I'm PyBot, your Python assistant! 🤖",
    "bye": "Goodbye! Have a great day! 👋",
    "who created you": "I was built by a smart B.Tech student like you 😎",
    "help": "You can try saying 'hi', 'how are you', 'bye', or ask about weather!",
    "weather": "It's always sunny in the world of code ☀️"
}

while True:
    user_input = input("You: ").lower()

    if user_input in responses:
        print("🤖 ChatBot:", responses[user_input])
        if user_input == "bye":
            break
    else:
        print("🤖 ChatBot: Sorry, I don't understand that. Try saying 'help'.")