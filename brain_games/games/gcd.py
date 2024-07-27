import random


def gcd(a, b):
    while b:
        a, b = b, a % b
    return a


def generate_question_and_answer():
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    correct_answer = gcd(random1, random2)
    question = f'{random1} {random2}'
    return question, correct_answer
