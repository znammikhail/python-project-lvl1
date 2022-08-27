"""brain-even game."""
import prompt
import random
from brain_games.games_logic import welcome_user, result, NUMBER_OF_ROUNDS


def brain_even():
    """brain-even game."""
    name = welcome_user()
    print('Answer "yes" if the number is even, otherwise answer "no".')
    count = 0
    while count < NUMBER_OF_ROUNDS:
        number = random.randint(1, 100)
        print(f'Question: {number}')
        correct_answer = ''
        if number % 2 == 0:
            correct_answer = 'yes'
        else:
            correct_answer = 'no'
        answer = prompt.string('Your answer: ')
        count = result(answer, correct_answer, name, count)
