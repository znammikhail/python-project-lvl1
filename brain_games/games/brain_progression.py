"""brain-progression game."""
import prompt
import random
from brain_games.games_logic import welcome_user, result, NUMBER_OF_ROUNDS


def brain_progression():
    """brain-progression game."""
    name = welcome_user()
    print('What number is missing in the progression?')

    count = 0
    while count < NUMBER_OF_ROUNDS:

        len = random.randint(5, 15)
        step = random.randint(1, 10)
        a = random.randint(1, 100)
        b = a + step * len + 1
        seq = list(range(a, b, step))
        index = random.randint(0, len - 1)
        correct_answer = seq[index]
        seq[index] = '..'
        seq = ' '.join(map(str, seq))
        print(f'Question: {seq}')
        answer = prompt.integer('Your answer: ')
        count = result(answer, correct_answer, name, count)
