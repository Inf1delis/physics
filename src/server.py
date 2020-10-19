from pprint import pprint

import telebot

from app.commands import new_group_command, start_lesson_command, search_command
from app.db import init_databases
from app.settings import load_config, CONFIG
from app.settings.consts import TOKEN, DEBUG
from app.keyboard import keyboard_builder
import telebot
bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['id'])
def handle_id(message: telebot.types.Message):
    if DEBUG:
        pprint(message.json)
    response_id = message.from_user.id
    response_text = response_id  # возвращаем user id
    reply_keyboard = keyboard_builder(2)
    bot.send_message(message.chat.id, response_text, reply_markup=reply_keyboard)


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
    bot.send_message(message.chat.id, response_text)


if __name__ == '__main__':
    load_config()
    init_databases(CONFIG)
    bot.polling(none_stop=False, interval=0, timeout=20)
