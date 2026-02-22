"""
=========================================================
            GENERAL KNOWLEDGE QUIZ GAME
---------------------------------------------------------
Author: Your Name
Description:
A simple interactive console-based quiz game built
using Python. The program asks multiple-choice questions,
keeps score, and displays correct answers at the end.

Concepts Used:
- Variables
- Functions
- Loops
- If-Else Statements
=========================================================
"""

# -------------------------------
# Function to display welcome UI
# -------------------------------
def display_welcome():
    print("=" * 55)
    print("        🎯 GENERAL KNOWLEDGE QUIZ GAME")
    print("=" * 55)
    print("Instructions:")
    print("• There are 3 multiple-choice questions.")
    print("• Type A, B, C, or D to answer.")
    print("• Each correct answer gives +1 point.")
    print("=" * 55)
    print()


# -----------------------------------------
# Function to ask a single quiz question
# -----------------------------------------
def ask_question(question_data):
    """
    Takes a dictionary containing:
    - question
    - options
    - correct answer

    Returns:
    - 1 if correct
    - 0 if incorrect
    """

    print("\n" + "-" * 55)
    print(question_data["question"])
    print("-" * 55)

    for option in question_data["options"]:
        print(option)

    # Take user input
    user_answer = input("\nYour answer (A/B/C/D): ").strip().upper()

    # Validate input
    if user_answer not in ["A", "B", "C", "D"]:
        print("⚠ Invalid input! Question marked incorrect.")
        return 0

    # Check answer
    if user_answer == question_data["correct"]:
        print("✅ Correct!")
        return 1
    else:
        print("❌ Incorrect!")
        return 0


# -------------------------------
# Function to run the quiz
# -------------------------------
def run_quiz():
    score = 0

    # Quiz Questions Data
    questions = [
        {
            "question": "1. What is the capital of India?",
            "options": [
                "A. Mumbai",
                "B. New Delhi",
                "C. Kolkata",
                "D. Chennai"
            ],
            "correct": "B",
            "correct_text": "New Delhi"
        },
        {
            "question": "2. Which planet is known as the Red Planet?",
            "options": [
                "A. Earth",
                "B. Venus",
                "C. Mars",
                "D. Jupiter"
            ],
            "correct": "C",
            "correct_text": "Mars"
        },
        {
            "question": "3. Who wrote the national anthem of India?",
            "options": [
                "A. Rabindranath Tagore",
                "B. Mahatma Gandhi",
                "C. Subhash Chandra Bose",
                "D. Jawaharlal Nehru"
            ],
            "correct": "A",
            "correct_text": "Rabindranath Tagore"
        }
    ]

    # Loop through each question
    for question in questions:
        score += ask_question(question)

    # Display final results
    print("\n" + "=" * 55)
    print("                🏁 QUIZ COMPLETED")
    print("=" * 55)
    print(f"Your Final Score: {score} / {len(questions)}")
    print("\nCorrect Answers:")

    for q in questions:
        print(f"{q['question']} → {q['correct_text']}")

    print("=" * 55)

    # Performance feedback
    if score == 3:
        print("🌟 Excellent performance!")
    elif score == 2:
        print("👍 Good job!")
    else:
        print("📚 Keep learning and try again!")


# -------------------------------
# Main Program Execution
# -------------------------------
if __name__ == "__main__":
    display_welcome()
    run_quiz()