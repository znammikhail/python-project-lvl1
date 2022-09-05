"""brain-prime game."""
import random


DESCRIPTION = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(n):
    """Prime number or not."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n


def correct_answer(simple):
    """Return correct answer."""
    return 'yes' if is_prime(simple) else 'no'


def make_question():
    """Generate game question."""
    simple = random.randint(1, 100)
    question = f'Question: {simple}'
    answer = correct_answer(simple)
    return (question, answer)
