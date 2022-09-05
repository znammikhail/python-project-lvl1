"""Brain-gcd game."""
import random


DESCRIPTION = 'Find the greatest common divisor of given numbers.'


def gcd(a, b):
    """Find gcd, return gcd."""
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def correct_answer(number_1, number_2):
    """Return correct answer."""
    return str(gcd(number_1, number_2))


def make_question():
    """Generate game question."""
    number_1 = random.randint(1, 100)
    number_2 = random.randint(1, 100)
    question = f'Question: {number_1} {number_2}'
    answer = correct_answer(number_1, number_2)
    return (question, answer)
