import prompt
import random


def bool_function(number):
    return number % 2 == 0


def play_even_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Answer "yes" if the number is even, otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if bool_function(number) else 'no'
        if user_answer == correct_answer:
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
