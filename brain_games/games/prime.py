import random
import prompt


def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, int(number**0.5) + 1):
        if number % i == 0:
            return False
    return True


def play_prime_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    correct_answers = 0
    while correct_answers < 3:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        user_answer = prompt.string('Your answer: ')

        correct_answer = 'yes' if is_prime(number) else 'no'

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
