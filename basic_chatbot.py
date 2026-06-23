def chatbot():

    print("=================================")
    print("      WELCOME TO CHATBOT")
    print("=================================")
    print("Type 'bye' to exit the chatbot.\n")

    while True:

        user = input("You: ").lower()

        if user == "hello":
            print("Bot: Hi!")

        elif user == "how are you":
            print("Bot: I'm fine, thanks!")

        elif user == "what is your name":
            print("Bot: My name is ChatBot.")

        elif user == "who created you":
            print("Bot: I was created using Python.")

        elif user == "bye":
            print("Bot: Goodbye!")
            break

        else:
            print("Bot: Sorry, I don't understand.")


# Start chatbot
chatbot()