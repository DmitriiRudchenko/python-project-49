import random

import sympy
from brain_games.main_logic import all_games_logic

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():
    end_number = 50
    numb = random.randint(0, end_number)
    number_f =f'{numb}!'
    if sympy.isprime(numb):
        meaning = 'yes'
    else:
        meaning = 'no'

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
