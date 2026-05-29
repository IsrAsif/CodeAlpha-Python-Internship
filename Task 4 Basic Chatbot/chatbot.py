# ============================================================
# TASK 4: Basic Chatbot
# Intern   : Isra Asif  |  ID: CA/DF1/54477
# Internship: CodeAlpha — Python Programming (May 2026)
# ============================================================


# ---------- 1. Rules: keywords → reply ---------------------
# Each entry: list of trigger keywords → response string
RULES = [
    # Greetings
    (["hello", "hi", "hey", "howdy", "greetings"],
     "Hi there! 👋 How can I help you today?"),

    # How are you
    (["how are you", "how r you", "how are u", "how do you do", "you okay"],
     "I'm doing great, thanks for asking! 😊 How about you?"),

    # User replies they're fine
    (["i'm fine", "im fine", "i am fine", "good", "great", "not bad", "doing well"],
     "That's wonderful to hear! 🌟 Is there anything I can help you with?"),

    # Name
    (["what is your name", "what's your name", "who are you", "your name"],
     "I'm ChatBot, your friendly assistant made by Isra Asif! 🤖"),

    # Age
    (["how old are you", "what is your age", "your age"],
     "I'm ageless — I was just born from a Python script! 😄"),

    # What can you do
    (["what can you do", "help", "capabilities", "what do you do"],
     "I can chat with you, answer basic questions, and keep you company! 💬"),

    # Time / Date
    (["what time is it", "current time", "what's the time"],
     "I don't have a clock, but your system tray definitely does! ⏰"),

    (["what is today", "what day is it", "today's date", "current date"],
     "I can't check the calendar, but your computer can tell you instantly! 📅"),

    # Jokes
    (["tell me a joke", "joke", "make me laugh", "say something funny"],
     "Why do programmers prefer dark mode? Because light attracts bugs! 🐛😂"),

    # Favourite things
    (["favorite color", "favourite color"],
     "I love the color of a perfectly running terminal — classic black! 🖥️"),

    (["favorite language", "favourite language", "best language"],
     "Python, of course! Clean, simple, and powerful. 🐍"),

    # Compliments
    (["you are great", "you're great", "you are good", "you're good",
      "nice", "awesome", "amazing", "well done"],
     "Aw, thank you so much! You're pretty awesome yourself! 😊"),

    # Insults / negative
    (["you are bad", "you're bad", "you are stupid", "you're stupid", "useless"],
     "That's okay! I'm still learning. I'll try to do better! 💪"),

    # Thanks
    (["thank you", "thanks", "thank u", "thx", "ty"],
     "You're welcome! Happy to help anytime. 😊"),

    # Bye
    (["bye", "goodbye", "see you", "see ya", "exit", "quit", "later", "take care"],
     "Goodbye! It was great chatting with you. Take care! 👋"),
]

# Fallback reply when nothing matches
FALLBACK = "Hmm, I'm not sure about that. 🤔 Try asking something else!"


# ---------- 2. Find a matching reply -----------------------
def get_reply(user_input: str) -> str:
    text = user_input.lower().strip()

    for keywords, reply in RULES:
        for keyword in keywords:
            if keyword in text:
                return reply

    return FALLBACK


# ---------- 3. Check if user wants to exit -----------------
def wants_to_exit(user_input: str) -> bool:
    exit_words = ["bye", "goodbye", "exit", "quit", "see you", "see ya", "later"]
    text = user_input.lower().strip()
    return any(word in text for word in exit_words)


# ---------- 4. Main chat loop ------------------------------
def main() -> None:
    print("\n" + "=" * 50)
    print("       🤖  CHATBOT — CodeAlpha Task 4")
    print("        Made by Isra Asif | CA/DF1/54477")
    print("=" * 50)
    print("  Type a message to start chatting.")
    print("  Type 'bye' to exit.\n")

    while True:
        user_input = input("  You     : ").strip()

        if not user_input:
            print("  ChatBot : Please type something! 😊\n")
            continue

        reply = get_reply(user_input)
        print(f"  ChatBot : {reply}\n")

        if wants_to_exit(user_input):
            break


if __name__ == "__main__":
    main()
