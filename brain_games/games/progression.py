import random

from brain_games.main_logic import all_games_logic

rules = 'What number is missing in the progression?'


def game_logic():
    first_number = random.randint(0, 200)
    second_number = random.randint(0, 300)
    step = random.randint(1, 10)

    if first_number > second_number:
        first_number, second_number = second_number, first_number

    a = list(range(first_number, second_number, step))

    if len(a) < 5:
        return game_logic()

    b = a[:10]
    b_len = len(b)
    random_number = random.randint(0, b_len - 1)
    meaning = b[random_number]
    secret = '..'
    b[random_number] = secret
    number_f = b

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)