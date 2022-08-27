"""brain-gcd game."""
import prompt
import random
from brain_games.games_logic import welcome_user, result, gcd, NUMBER_OF_ROUNDS


def brain_gcd():
    """brain-gcd game."""
    name = welcome_user()
    print('Find the greatest common divisor of given numbers.')

    count = 0
    while count < NUMBER_OF_ROUNDS:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        print(f'Question: {number_1} {number_2}')
        answer = prompt.integer('Your answer: ')
        correct_answer = gcd(number_1, number_2)
        count = result(answer, correct_answer, name, count)
