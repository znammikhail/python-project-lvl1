"""brain-prime game."""
import prompt
import random
from brain_games.games_logic import welcome_user, result
from brain_games.games_logic import is_prime, NUMBER_OF_ROUNDS


def brain_prime():
    """brain-prime game."""
    name = welcome_user()
    print('Answer "yes" if given number is prime. Otherwise answer "no".')

    count = 0
    while count < NUMBER_OF_ROUNDS:
        simple = random.randint(1, 100)
        print(f'Question: {simple}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if is_prime(simple) else 'no'
        count = result(answer, correct_answer, name, count)
