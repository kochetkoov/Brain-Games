import prompt
import random


def is_even(number):
    return number % 2 == 0


def play_even_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if the number is even, otherwise answer "no".')

    CORRECT_ANSWERS = 0

    while CORRECT_ANSWERS < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_even(number) else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            CORRECT_ANSWERS += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
