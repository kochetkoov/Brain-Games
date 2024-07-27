import random
import operator


def generate_question_and_answer():
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    if operation == '+':
        answer = operator.add(random1, random2)
    elif operation == '-':
        answer = operator.sub(random1, random2)
    else:
        answer = operator.mul(random1, random2)
    question = f'{random1} {operation} {random2}'
    return question, answer
