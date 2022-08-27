"""brain-calc game."""
import prompt
import random
from brain_games.games_logic import welcome_user, result, NUMBER_OF_ROUNDS


def brain_calc():
    """brain-calc game."""
    name = welcome_user()
    print('What is the result of the expression?')

    count = 0
    while count < NUMBER_OF_ROUNDS:
        number_1 = random.randint(1, 100)
        number_2 = random.randint(1, 100)
        operat = random.choice(['+', '-', '*'])
        print(f'Question: {number_1} {operat} {number_2}')
        answer = prompt.integer('Your answer: ')
        if operat == '+':
            correct_answer = number_1 + number_2
        if operat == '-':
            correct_answer = number_1 - number_2
        if operat == '*':
            correct_answer = number_1 * number_2
        count = result(answer, correct_answer, name, count)
