#!/usr/bin/env python3
"""Run brain-even game."""
from brain_games.games import brain_even
from brain_games.games_logic import engine


def main():
    """Run brain-even game."""
    engine(brain_even)


if __name__ == '__main__':
    main()
