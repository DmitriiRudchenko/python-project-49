
from brain_games.main_logic import all_games_logic

import random


rules = 'What is the result of the expression?'


def game_logic():
    number_f = random.randint(0, 50)
    if number_f % 2 == 0:
        meaning = 'yes'
    else:
        meaning = 'no'

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
