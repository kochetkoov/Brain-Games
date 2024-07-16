import random
import prompt


def play_progression_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print("What number is missing in the progression?")

    correct_answers = 0
    while correct_answers < 3:
        start = random.randint(1, 10)
        step = random.randint(1, 10)
        length = 10
        progression = [start + step * i for i in range(length)]
        missing_index = random.randint(0, length - 1)
        correct_answer = progression[missing_index]
        progression[missing_index] = ".."
        print("Question: " + " ".join(map(str, progression)))
        user_answer = prompt.string("Your answer: ")

        if int(user_answer) == correct_answer:
            print("Correct!")
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(. "
                f"Correct answer was '{correct_answer}'.")
            print(f"Let's try again, {name}!")
            return

    print(f"Congratulations, {name}!")
