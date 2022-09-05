#!/usr/bin/env python3
"""Run brain-gcd game."""
from brain_games.games import brain_gcd
from brain_games.games_logic import engine


def main():
    """Run brain-gcd game."""
    engine(brain_gcd)


if __name__ == '__main__':
    main()
