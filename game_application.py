
import random

# Store the quiz questions
questions = [
    {
        "question": "Which african contry does not require a visa?",
        "choices": {
            "A": "Nigeria",
            "B": "Namibia",
            "C": "South Africa",
            "D": "Seychelles"
        },
        "answer": "C"
    },
    {
        "question": "Which language is commonly used for Python development?",
        "choices": {
            "A": "Python",
            "B": "HTML",
            "C": "CSS",
            "D": "SQL"
        },
        "answer": "A"
    },
    {
        "question": "What is 5 * 3?",
        "choices": {
            "A": "6",
            "B": "7",
            "C": "8",
            "D": "15"
        },
        "answer": "D"
    },
    {
        "question": "Which of the below is not amang the reserved keywords in Python?",
        "choices": {
            "A": "if",
            "B": "define",
            "C": "fun",
            "D": "def"
        },
        "answer": "C"
    },
    {
        "question": "Which data type stores text characters?",
        "choices": {
            "A": "String",
            "B": "Boolean",
            "C": "List",
            "D": "Integer"
        },
        "answer": "A"
    }
]


def play_quiz():
    score = 0
    total_questions = len(questions)

    # Mix up the order of the questions
    random.shuffle(questions)

    print("=" * 40)
    print("       WELCOME TO THE QUIZ GAME!")
    print("=" * 40)
    print("Choose A, B, C, or D for each question.\n")

    # Display questions one by one
    for number, item in enumerate(questions, start=1):
        print(f"Question {number}: {item['question']}")

        for letter, choice in item["choices"].items():
            print(f"  {letter}. {choice}")

        # Validate the user's input
        while True:
            try:
                user_answer = input("Your answer (A/B/C/D): ").strip().upper()

                if user_answer not in ["A", "B", "C", "D"]:
                    raise ValueError(
                        "Please enter only A, B, C, or D."
                    )

                break

            except ValueError as error:
                print(f"Invalid input: {error}")

        # Check the answer and update the score
        if user_answer == item["answer"]:
            print("Correct! Well done!\n")
            score += 1
        else:
            correct_answer = item["answer"]
            correct_choice = item["choices"][correct_answer]
            print(
                f"Incorrect! The correct answer is "
                f"{correct_answer}. {correct_choice}\n"
            )

    # Display the final results
    percentage = (score / total_questions) * 100

    print("=" * 40)
    print("             QUIZ RESULTS")
    print("=" * 40)
    print(f"Your score: {score}/{total_questions}")
    print(f"Percentage: {percentage:.0f}%")

    if percentage >= 80:
        print("Feedback: Excellent! 🎉")
    elif percentage >= 50:
        print("Feedback: Good! Keep practising.")
    else:
        print("Feedback: Try Again! You can do it.")

    print("=" * 40)


# Start the game
if __name__ == "__main__":
    play_quiz()
