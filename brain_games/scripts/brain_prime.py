#!/usr/bin/env python3
"""Run brain-prime game."""
from brain_games.games import brain_prime
from brain_games.games_logic import engine


def main():
    """Run brain-prime game."""
    engine(brain_prime)


if __name__ == '__main__':
    main()
