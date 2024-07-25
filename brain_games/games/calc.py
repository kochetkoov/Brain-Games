import prompt
import random
import operator


def play_calc_game():
    print("Welcome to the Brain Games!")
    name = prompt.string("May I have your name? ")
    print(f"Hello, {name}!")
    print('What is the result of the expression?')

    correct_answers = 0
    operations = ['+', '-', '*']

    while correct_answers < 3:
        random1 = random.randint(1, 100)
        random2 = random.randint(1, 100)
        operation = random.choice(operations)
        if operation == '+':
            correct_answer = operator.add(random1, random2)
        elif operation == '-':
            correct_answer = operator.sub(random1, random2)
        else:
            correct_answer = operator.mul(random1, random2)

        print(f'Question: {random1} {operation} {random2}')
        answer = prompt.string('Your answer: ')
        if answer == str(correct_answer):
            print('Correct!')
            correct_answers += 1
        else:
            print(
                f"'{answer}' is wrong answer ;(."
                f"Correct answer was '{correct_answer}'")
            print(f"Let's try again, {name}!")
            return

    print(f'Congratulations, {name}!')
