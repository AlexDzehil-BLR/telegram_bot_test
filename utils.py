from emoji import emojize
from telegram import ReplyKeyboardMarkup, KeyboardButton
from random import randint, choice

import settings

def get_smile(user_data):
    if 1 not in user_data:
        smile = choice(settings.USER_EMOJI)
        return emojize(smile, use_aliases=True)
    return user_data[1]

def play_random_numbers(user_number):
    my_number = randint(user_number - 10, user_number + 10)
    if user_number > my_number:
        message = f'Ты загадал {user_number}, я загадал {my_number}, ты победил!'
    elif user_number == my_number:
        message = f'Ты загадал {user_number}, я загадал {my_number}, ничья!'
    else:
        message = f'Ты загадал {user_number}, я загадал {my_number}, я победил!'
    return message


def main_keyboard():
    return ReplyKeyboardMarkup([['Прислать Чувака', KeyboardButton('Мои координаты', request_location=True)]])