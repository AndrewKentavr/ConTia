from aiogram import types
from aiogram.utils import emoji


def get_keyboard_logic_start():
    buttons = [
        'Задания из категорий Логики',
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    return keyboard


def get_keyboard_logic_category():
    buttons = [
        emoji.emojize(":arrow_right:") + ' Следующая задача логика',
        emoji.emojize(":stop_sign:") + ' Закончить логику'
    ]
    keyboard = types.ReplyKeyboardMarkup(resize_keyboard=True, row_width=2)
    keyboard.add(*buttons)
    return keyboard
