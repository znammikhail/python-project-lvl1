"""brain-progression game."""
import random


RULES = 'What number is missing in the progression?'
DIFFERENCE = 10
MAX_COUNT_NUM = 15
MAX_VALUE = 100


def make_progression(a, d, n):
    """Create progression."""
    a_n = a + d * n + 1
    ap = list(range(a, a_n, d))
    return ap


def make_string(ap):
    """Create string."""
    ap_string = ' '.join(map(str, ap))
    return ap_string


def correct_answer(seq):
    """Return correct answer."""
    index = random.randint(0, len(seq) - 1)
    return str(seq[index])


def question_and_answer():
    """Generate game question and correct anweer."""
    n = random.randint(5, MAX_COUNT_NUM)
    d = random.randint(1, DIFFERENCE)
    a = random.randint(1, MAX_VALUE)
    ap = make_progression(a, d, n)
    answer = correct_answer(ap)
    ap_string = make_string(ap)
    ap_string = ap_string.replace(answer, '..')
    question = f'{ap_string}'
    return (question, answer)
