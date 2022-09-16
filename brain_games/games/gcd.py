import random
import math

from brain_games.main_logic import all_games_logic

rules = 'Find the greatest common divisor of given numbers.'


def game_logic():
    first_number = random.randint(0, 50)
    second_number = random.randint(0, 50)
    number_f = f'{first_number} {second_number}'
    meaning = math.gcd(first_number, second_number)
    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)