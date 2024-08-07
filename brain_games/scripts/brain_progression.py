#!/usr/bin/env python3

from brain_games.games.progression import generate_question_and_answer
from brain_games.games.progression import DESCRIPTION
from brain_games.engine import play_game


def main():
    play_game(DESCRIPTION, generate_question_and_answer)


if __name__ == '__main__':
    main()
