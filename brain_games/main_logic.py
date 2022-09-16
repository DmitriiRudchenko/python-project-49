

import prompt

name = ''


def welcome_user():
    global name
    print('Welcome to the Brain Games!')
    name1 = prompt.string('May I have your name? ')
    print(f'Hello, {name1}!')
    name = name1


def win_ending():
    print(f'Congratulations, {name}!')


def lose_ending(answer, meaning):
    print(f"'{answer}' is wrong answer ;(. Correct answer was '{meaning}'.\nLet's try again, {name}!")


def all_games_logic(rules, game_logic):
    welcome_user()
    print(rules)

    def ask2(number_of_answers=0):
        if number_of_answers > 2:
            return win_ending()

        qa = game_logic()
        question = qa[0]
        correct_answer = qa[1]

        print(f'Question: {question}')
        answer = prompt.string('Your answer: ')

        if str(answer) != str(correct_answer):
            return lose_ending(answer, correct_answer)

        print('Correct!')
        number_of_answers += 1

        ask2(number_of_answers)

    ask2()
