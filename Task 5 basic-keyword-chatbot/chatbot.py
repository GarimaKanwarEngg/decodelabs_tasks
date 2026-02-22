"""
=========================================================
                BASIC KEYWORD CHATBOT
---------------------------------------------------------
Author: Your Name
Description:
A simple rule-based chatbot built using Python.
The chatbot responds to specific keywords using
case-insensitive matching.

Concepts Used:
- While loop (infinite loop)
- If-elif-else statements
- String matching
- Loop control (break)
- Functions
=========================================================
"""


# -----------------------------------------
# Function to generate chatbot response
# -----------------------------------------
def get_response(user_input):
    """
    Takes user input as a string.
    Returns appropriate chatbot response
    based on keyword matching.
    """

    # Convert input to lowercase for case-insensitive matching
    message = user_input.lower()

    # Rule-based keyword matching
    if message == "hello":
        return "Hi there!"

    elif message == "bye":
        return "Goodbye! Have a great day!"

    else:
        return "I don't understand."


# -----------------------------------------
# Main chatbot execution loop
# -----------------------------------------
def run_chatbot():
    """
    Runs the chatbot in an infinite loop
    until user types 'bye'.
    """

    print("=" * 50)
    print("🤖 BASIC KEYWORD CHATBOT")
    print("=" * 50)
    print("Type 'hello' to greet.")
    print("Type 'bye' to exit.")
    print("=" * 50)

    while True:  # Infinite loop
        user_input = input("\nYou: ")

        response = get_response(user_input)

        print("Bot:", response)

        # Exit condition
        if user_input.lower() == "bye":
            break


# -----------------------------------------
# Program Entry Point
# -----------------------------------------
if __name__ == "__main__":
    run_chatbot()