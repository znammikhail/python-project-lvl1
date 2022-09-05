#!/usr/bin/env python3
"""Run brain-calc game."""
from brain_games.games import brain_calc
from brain_games.games_logic import engine


def main():
    """Run brain-calc game."""
    engine(brain_calc)


if __name__ == '__main__':
    main()
