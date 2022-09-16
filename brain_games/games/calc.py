import random

from brain_games.main_logic import all_games_logic

rules = 'What is the result of the expression?'


def game_logic():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)
    operations = random.randint(0, 2)
    if operations == 0:
        number_f = f'{first_number} + {second_number}'
        meaning = first_number + second_number
    if operations == 1:
        number_f = f'{first_number} - {second_number}'
        meaning = first_number - second_number
    if operations == 2:
        number_f = f'{first_number} - {second_number}'
        meaning = first_number - second_number
    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
