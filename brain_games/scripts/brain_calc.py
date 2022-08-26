#!/usr/bin/env python3
import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What is the result of the expression?')
    count = 0
    while count < 3:
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        operat = random.choice(['+', '-', '*'])
        print(f'Question: {number_1} {operat} {number_2}')
        answer = prompt.integer('Your answer: ')
        if operat == '+':
            correct_answer = number_1 + number_2
        if operat == '-':
            correct_answer = number_1 - number_2
        if operat == '*':
            correct_answer = number_1 * number_2

        if answer == correct_answer:
            print('Corerct!')
            count += 1
        else:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{correct_answer}'.\nLet's try again, {name}!")            
            count = 10
        if count == 3:
            print(f'Congratulations, {name}!')
            

if __name__ == '__main__':
    main()