# This is an AI Chatbot Program that responds to User's Input with Predefined statements.

statements = {
    "hello": "Hello, How can I help you today?",
    "hi": "Hi, What can I do for you today?",
    "how are you?": "I'm doing fine, thank you!",
    "good morning": "Good morning! How can I help you today?",
    "good night": "Good Night! Have a great day tomorrow!",
    "thank you": "You're Welcome!",
    "thanks": "Glad I could help.",
    "who are you?": "I am an AI Chatbot designed to help you.",
    "what is a chatbot?": "A Chatbot is a program designed to simulate conversation with human users.",
    "bye": "Goodbye! Have a great day!",
    "what is ai?": "AI stands for Artificial Intelligence and it refers to the simulation of human thinking."
}

while True: 
    user_input = input("Enter your message: ").strip().lower()

    if user_input == "exit":
        print("Exiting the program. Goodbye!")
        break

    print(statements.get(user_input,"Sorry, I can't help you with it."))
