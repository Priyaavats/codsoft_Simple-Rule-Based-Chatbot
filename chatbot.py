# Simple Rule-Based Chatbot

def chatbot():
    print("Chatbot: Hello! Type 'bye' to exit.")
    while True:
        user_input = input("You: ").lower()

        if user_input == "hello":
            print("Chatbot: Hi there! How can I help you?")
        elif user_input == "how are you":
            print("Chatbot: I'm just a program, but I'm doing great!")
        elif user_input == "bye":
            print("Chatbot: Goodbye! Have a great day!")
            break
        else:
            print("Chatbot: Sorry, I don't understand that.")

chatbot()
