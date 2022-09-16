import random
import math

from brain_games.main_logic import all_games_logic

rules = 'Answer "yes" if given number is prime. Otherwise answer "no".'


def is_prime(number):
    for numbers in range(2, int(math.sqrt(number)) + 1):
        if (number % numbers) == 0:
            return False
        return True


def game_logic():
    end_number = 50
    number_f = random.randint(2, end_number)

    if is_prime(number_f):
        meaning = 'yes'
    else:
        meaning = 'no'

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
