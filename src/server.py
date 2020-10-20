from pprint import pprint

import telebot

from app.commands import new_group_command, start_lesson_command, search_command, score_command
from app.db import init_databases
from app.keyboard import keyboard_builder, GREETING_MESSAGE
from app.settings import load_config, CONFIG
from app.settings.consts import TOKEN, DEBUG
import telebot

bot = telebot.TeleBot(TOKEN)


@bot.callback_query_handler(func=lambda call: True)
def call_back_room(c: telebot.types.CallbackQuery):
    """

    :param c:
    :return:
    """
    # import pydevd_pycharm
    # pydevd_pycharm.settrace('localhost', port=2001, stdoutToServer=True, stderrToServer=True)
    response_text = score_command(c.message.from_user.id, c.data)
    bot.send_message(c.message.chat.id, response_text)


@bot.message_handler(commands=['id'])
def handle_id(message: telebot.types.Message):
    if DEBUG:
        pprint(message.json)
    response_id = message.from_user.id
    response_text = response_id  # возвращаем user id
    bot.send_message(message.chat.id, response_text)


@bot.message_handler(commands=['newGroup'])
def handle_new_group(message: telebot.types.Message):
    if DEBUG:
        pprint(message.json)
    response_text = new_group_command(message)
    bot.send_message(message.chat.id, response_text)


@bot.message_handler(commands=['startLesson'])
def handle_start_lesson(message: telebot.types.Message):
    if DEBUG:
        pprint(message.json)

    response_text = start_lesson_command(message)
    bot.send_message(message.chat.id, response_text)


@bot.message_handler(commands=['search'])
def handle_search(message: telebot.types.Message):
    if DEBUG:
        pprint(message.json)
    response_text = search_command(message)
    if isinstance(response_text, list):
        for name in response_text:
            reply_keyboard = keyboard_builder(name)
            bot.send_message(message.chat.id, name, reply_markup=reply_keyboard)
    else:
        bot.send_message(message.chat.id, response_text)

@bot.message_handler(commands=['start'])
def handler_start(message: telebot.types.Message):
    """
    Метод старта бота. Нужен для отправки кнопок
    :param message:
    :return:
    """
    if DEBUG:
        pprint(message.json)
    response_text = GREETING_MESSAGE
    bot.send_message(message.chat.id, response_text)


# @bot.message_handler(commands=['help'])
# def handler_help(message: telebot.types.Message):
#     """
#     Справочный метод для помощи пользователям
#     :param message:
#     :return:
#     """
#     if DEBUG:
#         pprint(message.json)
#     response_text =
if __name__ == '__main__':
    load_config()
    init_databases(CONFIG)
    bot.polling(none_stop=False, interval=0, timeout=20)
