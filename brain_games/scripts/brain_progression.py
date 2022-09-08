#!/usr/bin/env python3
"""Run brain-progression game."""
from brain_games.games import brain_progression
from brain_games.engine import start_engine


def main():
    """Run brain-progression game."""
    start_engine(brain_progression)


if __name__ == '__main__':
    main()
