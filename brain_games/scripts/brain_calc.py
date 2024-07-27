#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.calc import generate_question_and_answer

DESCRIPTION = 'What is the result of the expression?'


def main():
    play_game(DESCRIPTION, generate_question_and_answer)


if __name__ == '__main__':
    main()
