from telebot.types import ReplyKeyboardMarkup, KeyboardButton
from app.settings.consts import *


def keyboard_builder(count_of_buttons):
    """
    Формирование кнопочек
    :return:
    """
    reply_key_board = ReplyKeyboardMarkup(resize_keyboard=True)
    buttons = DICT_OF_BUTTONS[count_of_buttons]
    for button in buttons:
        button = KeyboardButton(text=button)
        reply_key_board.add(button)
    return reply_key_board
