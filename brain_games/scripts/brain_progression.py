import prompt
import random


def main():
    print('Welcome to the Brain Games!')
    name = prompt.string('May I have your name? ')
    print(f'Hello, {name}!')
    print('What number is missing in the progression?')
    count = 0
    while count < 3:

        len = random.randint(5,15)
        step = random.randint(1,10)
        a = random.randint(1,100)
        b = a + step*len + 1
        seq = list(range(a, b, step))
        index = random.randint(0, len-1)
        correct_answer = seq[index]
        seq[index] = '..'
        seq = ' '.join(map(str,seq))
        print(f'Question: {seq}')
        answer = prompt.integer('Your answer: ')

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