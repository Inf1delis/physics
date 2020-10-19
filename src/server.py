from pprint import pprint

import telebot

from app.commands import new_group_command
from app.db import init_databases
from app.settings import load_config, CONFIG
from app.settings.consts import TOKEN, DEBUG

bot = telebot.TeleBot(TOKEN)


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


if __name__ == '__main__':
    load_config()
    init_databases(CONFIG)
    bot.polling(none_stop=False, interval=0, timeout=20)
