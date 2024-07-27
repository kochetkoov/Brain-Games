#!/usr/bin/env python3

from brain_games.games.prime import generate_question_and_answer
from brain_games.engine import play_game

DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def main():
    play_game(DESCRIPTION, generate_question_and_answer)


if __name__ == '__main__':
    main()
