import random

QUESTIONS = [
    {"question": "Who created the Python language?",
     "options": ["Guido van Rossum", "James Gosling", "Dennis Ritchie", "Bjarne Stroustrup"], "answer": 1},
    {"question": "Which function prints output on the screen?",
     "options": ["input()", "print()", "output()", "show()"], "answer": 2},
    {"question": "Which symbol is used for a single-line comment?",
     "options": ["#", "//", "/*", "--"], "answer": 1},
    {"question": "What is the data type of [1, 2, 3]?",
     "options": ["tuple", "dict", "list", "set"], "answer": 3},
    {"question": "What is the output of 2 ** 3?",
     "options": ["6", "5", "9", "8"], "answer": 4},
    {"question": "Which keyword is used to define a function?",
     "options": ["func", "def", "function", "define"], "answer": 2},
    {"question": "What is the file extension of a Python file?",
     "options": [".py", ".pt", ".python", ".pyt"], "answer": 1},
    {"question": "What is len('Python')?",
     "options": ["5", "7", "6", "4"], "answer": 3},
    {"question": "Which loop repeats over a sequence?",
     "options": ["if", "for", "def", "import"], "answer": 2},
    {"question": "What is the capital of Jharkhand?",
     "options": ["Ranchi", "Dhanbad", "Jamshedpur", "Bokaro"], "answer": 1},
]


def ask_question(number, item):
    print(f"\nQ{number}. {item['question']}")
    for i, option in enumerate(item["options"], start=1):
        print(f"  {i}. {option}")

    while True:
        choice = input("Your answer (1-4): ").strip()
        if choice in ("1", "2", "3", "4"):
            return int(choice) == item["answer"]
        print("Please enter a number between 1 and 4.")


def get_result(score, total):
    percent = score / total * 100
    if percent >= 80:
        return "Excellent!"
    elif percent >= 50:
        return "Good, keep practicing!"
    else:
        return "Needs more practice."


def save_score(name, score, total):
    with open("scores.txt", "a") as file:
        file.write(f"{name}: {score}/{total}\n")


def main():
    print("=== Python Quiz Game ===")
    name = input("Enter your name: ").strip() or "Player"

    questions = QUESTIONS[:]
    random.shuffle(questions)

    score = 0
    for number, item in enumerate(questions, start=1):
        if ask_question(number, item):
            print("Correct!")
            score += 1
        else:
            correct_text = item["options"][item["answer"] - 1]
            print(f"Wrong! Correct answer: {correct_text}")

    total = len(questions)
    print(f"\n{name}, your score: {score}/{total}")
    print(get_result(score, total))
    save_score(name, score, total)


if __name__ == "__main__":
    main()
    
