"""Brain-even game."""
import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'


def correct_answer(number):
    """Return expected answer."""
    return 'yes' if number % 2 == 0 else 'no'


def make_question():
    """Generate game question."""
    number = random.randint(1, 100)
    question = f'Question: {number}'
    answer = correct_answer(number)
    return (question, answer)
