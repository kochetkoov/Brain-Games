import random


def is_even(number):
    return number % 2 == 0


def generate_question_and_answer():
    number = random.randint(1, 100)
    question = str(number)
    correct_answer = 'yes' if is_even(number) else 'no'
    return question, correct_answer
