#!/usr/bin/env python3
"""Run brain-progression game."""
from brain_games.games import brain_progression
from brain_games.games_logic import engine


def main():
    """Run brain-progression game."""
    engine(brain_progression)


if __name__ == '__main__':
    main()
