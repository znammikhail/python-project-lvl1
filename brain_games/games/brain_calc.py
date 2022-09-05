"""Brain-calc game."""
import random


DESCRIPTION = 'What is the result of the expression?'


def correct_answer(number_1, operat, number_2):
    """Return correct answer."""
    if operat == '+':
        correct_answer = number_1 + number_2
    if operat == '-':
        correct_answer = number_1 - number_2
    if operat == '*':
        correct_answer = number_1 * number_2
    return str(correct_answer)


def make_question():
    """Generate game question."""
    number_1 = random.randint(1, 20)
    number_2 = random.randint(1, 20)
    operat = random.choice(['+', '-', '*'])
    question = f'Question: {number_1} {operat} {number_2}'
    answer = correct_answer(number_1, operat, number_2)
    return (question, answer)
