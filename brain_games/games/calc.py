import random
import operator

DESCRIPTION = 'What is the result of the expression?'


def apply_operation(num1, num2, operation):
    if operation == '+':
        return operator.add(num1, num2)
    elif operation == '-':
        return operator.sub(num1, num2)
    else:
        return operator.mul(num1, num2)


def generate_question_and_answer():
    random1 = random.randint(1, 100)
    random2 = random.randint(1, 100)
    operation = random.choice(['+', '-', '*'])
    answer = apply_operation(random1, random2, operation)
    question = f'{random1} {operation} {random2}'
    return question, answer
