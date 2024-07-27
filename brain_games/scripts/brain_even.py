#!/usr/bin/env python3

from brain_games.engine import play_game
from brain_games.games.even import generate_question_and_answer

DESCRIPTION = 'Answer "yes" if the number is even, otherwise answer "no".'


def main():
    play_game(DESCRIPTION, generate_question_and_answer)


if __name__ == '__main__':
    main()
