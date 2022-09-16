import random

from brain_games.main_logic import all_games_logic

rules = 'Answer "yes" if the number is even, otherwise answer "no".'


def game_logic():
    end_number = 50
    number_f = random.randint(0, end_number)
    if number_f % 2 == 0:
        meaning = 'yes'
    else:
        meaning = 'no'

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
