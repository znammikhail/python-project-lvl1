#!/usr/bin/env python3
"""Game engine functions."""
import prompt

NUMBER_OF_ROUNDS = 3


def welcome_user():
    """Greeting user, return name user."""
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}')
    return name


def result(answer, correct_answer, name, count):
    """Answer user, return count."""
    if answer == correct_answer:
        print('Corerct!')
        count += 1
    else:
        print(f"'{answer}' is wrong answer ;(. ", end='')
        print(f"Correct answer was '{correct_answer}'.")
        print(f"Let's try again, {name}!")
        count = 10
    if count == 3:
        print(f'Congratulations, {name}!')
    return count


def engine(game):
    """Game engine function."""
    name = welcome_user()
    print(game.DESCRIPTION)
    count = 0
    while count < NUMBER_OF_ROUNDS:
        question, correct_answer = game.make_question()
        print(question)
        answer_user = prompt.string('Your answer: ')
        count = result(answer_user, correct_answer, name, count)
