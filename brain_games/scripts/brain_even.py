#!/usr/bin/env python3

import random
import prompt

name = ''
number_of_answers = 0 


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name1 = prompt.string('May I have your name? ')
    print(f'Hello, {name1}!')
    name = name1

def even_game():
    global number_of_answers
    number_f = random.randint(0, 50)
    meaning = ''
    print(f'Qestion: {number_f}')
    
    
    if number_f % 2 == 0:
        meaning = 'yes'
    else:
        meaning = 'no'


    answer = prompt.string('Your answer: ')

    
    if number_of_answers < 2:
        if answer == meaning:
            print('Correct!')
            number_of_answers += 1
            even_game()
        
        if answer != meaning:
            print(f"'{answer}' is wrong answer ;(. Correct answer was '{meaning}'.\nLet's try again, {name}")
    
    else:
        print(f'Congratulations, {name}!')


def main():
    print('Answer "yes" if the number is even, otherwise answer "no".')
    even_game()


if __name__ == '__main__':
    main()
