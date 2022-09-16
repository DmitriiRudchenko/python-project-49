import random

from brain_games.main_logic import all_games_logic

rules = 'What number is missing in the progression?'


def game_logic():
    max_first_number = 200
    max_second_number = 300
    first_number = random.randint(0, max_first_number)
    second_number = random.randint(0, max_second_number)
    step = random.randint(1, 10)

    if first_number > second_number:
        first_number, second_number = second_number, first_number

    created_progression = list(range(first_number, second_number, step))

    if len(created_progression) < 5:
        return game_logic()

    visible_progression = created_progression[:10]
    b_len = len(visible_progression)
    random_number = random.randint(0, b_len - 1)
    meaning = visible_progression[random_number]
    secret = '..'
    visible_progression[random_number] = secret
    number_f = ' '.join(map(str, visible_progression))

    return [number_f, meaning]


def export_func():
    all_games_logic(rules, game_logic)
