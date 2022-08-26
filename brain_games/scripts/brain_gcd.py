import prompt
import random


def gcd(a, b):
    while a != 0 and b != 0:
        if a > b:
            a = a % b
        else:
            b = b % a
    return(a + b)


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Find the greatest common divisor of given numbers.')
    count = 0
    while count < 3:
        number_1 = random.randint(1,100)
        number_2 = random.randint(1,100)
        print(f'Question: {number_1} {number_2}')
        answer = prompt.integer('Your answer: ')
        correct_answer = 1
        correct_answer = gcd(number_1, number_2)
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