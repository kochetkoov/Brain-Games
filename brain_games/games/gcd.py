import prompt
import random
import math


def play_gcd_game():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    print('Find the greatest common divisor of given numbers.')

    correct_answers = 0

    while correct_answers < 3:
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        print(f'Question: {random1} {random2}')
        user_answer = prompt.string('Your answer: ')
        correct_answer = math.gcd(random1, random2)
        if user_answer == str(correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}")
            return

    print(f'Congratulations, {name}!')
