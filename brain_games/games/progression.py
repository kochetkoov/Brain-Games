import random


def generate_question_and_answer():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    progression = [start + i * step for i in range(length)]
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    question = ' '.join(map(str, progression))
    return question, correct_answer
