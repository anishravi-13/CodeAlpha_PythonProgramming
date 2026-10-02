import datetime

def get_bot_response(user_input):
    """
    Evaluates user input using rule-based pattern matching (if-elif)
    and returns a predefined response.
    """
    message = user_input.lower().strip()

    # Greetings
    if any(greet in message for greet in ["hello", "hi", "hey", "greetings"]):
        return "Hi there! How can I help you today?"
    
    # Status / Well-being
    elif "how are you" in message or "how's it going" in message or "how do you do" in message:
        return "I'm fine, thanks! I am running smoothly. How about you?"

    # Name inquiries
    elif "your name" in message or "who are you" in message:
        return "I am AlphaBot, a rule-based Python chatbot created for the CodeAlpha internship!"

    # Time inquiries
    elif "time" in message or "date" in message:
        now = datetime.datetime.now()
        return f"The current date and time is: {now.strftime('%Y-%m-%d %H:%M:%S')}"

    # Help
    elif "help" in message:
        return (
            "I can answer basic questions! Try asking me:\n"
            "  - 'hello' or 'hi'\n"
            "  - 'how are you?'\n"
            "  - 'what is your name?'\n"
            "  - 'what time is it?'\n"
            "  - 'tell me a joke'\n"
            "  - 'bye' or 'exit'"
        )

    # Joke
    elif "joke" in message:
        return "Why do programmers prefer dark mode? Because light attracts bugs!"

    # Thank you
    elif "thank" in message:
        return "You're very welcome! Let me know if you need anything else."

    # Farewells
    elif any(bye in message for bye in ["bye", "goodbye", "exit", "quit", "see you"]):
        return "Goodbye! Have a wonderful day ahead!"

    # Fallback for unrecognized inputs
    else:
        return "I'm not sure I understand that. Type 'help' to see what I can answer or 'bye' to exit."

def start_chatbot():
    print("=" * 50)
    print("             ALPHABOT - BASIC CHATBOT")
    print("=" * 50)
    print("Chatbot initialized! Type 'bye' or 'exit' to end the chat.")
    print("=" * 50)

    while True:
        try:
            user_input = input("\nYou: ").strip()
            if not user_input:
                continue

            bot_reply = get_bot_response(user_input)
            print(f"AlphaBot: {bot_reply}")

            if any(bye in user_input.lower() for bye in ["bye", "goodbye", "exit", "quit"]):
                break

        except (KeyboardInterrupt, EOFError):
            print("\nAlphaBot: Goodbye!")
            break

if __name__ == "__main__":
    start_chatbot()
