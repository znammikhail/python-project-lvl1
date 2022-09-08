"""Brain-even game."""
import random


DESCRIPTION = 'Answer "yes" if number even otherwise answer "no".'
MAX_NUM = 100


def is_even(number):
    """Even number or not."""
    return number % 2 == 0


def correct_answer(number):
    """Return expected answer."""
    return 'yes' if is_even(number) else 'no'


def make_question():
    """Generate game question."""
    number = random.randint(1, MAX_NUM)
    question = f'{number}'
    answer = correct_answer(number)
    return (question, answer)
