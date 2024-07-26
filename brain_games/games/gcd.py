import prompt
import random
from brain_games.games.engine import hello_user


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def play_gcd_game():
    name = hello_user()
    print('Find the greatest common divisor of given numbers.')

    CORRECT_ANSWERS = 0

    while CORRECT_ANSWERS < 3:
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        correct_answer = gcd(random1, random2)

        print(f'Question: {random1} {random2}')
        user_answer = prompt.string('Your answer: ')

        if int(user_answer) == correct_answer:
            print('Correct!')
            CORRECT_ANSWERS += 1
        else:
            print(
                f"'{user_answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
