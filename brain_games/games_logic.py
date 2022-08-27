#!/usr/bin/env python3
"""logic games."""
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


def gcd(a, b):
    """Find gcd, return gcd."""
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return (a + b)


def is_prime(n):
    """Prime number or not."""
    d = 2
    while n % d != 0:
        d += 1
    return d == n
