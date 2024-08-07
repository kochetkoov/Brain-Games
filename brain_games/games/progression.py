import random


DESCRIPTION = "What number is missing in the progression?"


def generate_progression():
    start = random.randint(1, 10)
    step = random.randint(1, 10)
    length = 10
    progression = [start + i * step for i in range(length)]
    return progression


def generate_question_and_answer():
    progression = generate_progression()
    length = len(progression)
    missing_index = random.randint(0, length - 1)
    correct_answer = progression[missing_index]
    progression[missing_index] = ".."
    question = ' '.join(map(str, progression))
    return question, correct_answer
