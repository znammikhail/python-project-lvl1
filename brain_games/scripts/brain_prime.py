import prompt
import random


def IsPrime(n):
    d = 2
    while n % d != 0:
        d += 1
    return d == n

def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('Answer "yes" if given number is prime. Otherwise answer "no".')
    count = 0
    while count < 3:
        simple = random.randint(1,100)       
        print(f'Question: {simple}')
        answer = prompt.string('Your answer: ')
        correct_answer = 'yes' if IsPrime(simple) else 'no'
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