"""brain-progression game."""
import random


DESCRIPTION = 'What number is missing in the progression?'


def make_question():
    """Generate game question."""
    len = random.randint(5, 15)
    step = random.randint(1, 10)
    a = random.randint(1, 100)
    b = a + step * len + 1
    seq = list(range(a, b, step))
    index = random.randint(0, len - 1)
    correct_answer = seq[index]
    seq[index] = '..'
    question = f'Question: {seq}'
    answer = str(correct_answer)
    return (question, answer)
