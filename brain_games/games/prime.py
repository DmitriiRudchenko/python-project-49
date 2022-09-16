# import random

# import sympy
from brain_games.main_logic import all_games_logic

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def game_logic():

    number_f = 5
    meaning = 'yes'

    # end_number = 50
    # number_f = random.randint(2, end_number)

    # if sympy.isprime(number_f):
    #     meaning = 'yes'
    # else:
    #     meaning = 'no'

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
