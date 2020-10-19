import telebot

from app.settings import load_config
from app.settings.consts import TOKEN

bot = telebot.TeleBot(TOKEN)


@bot.message_handler(commands=['id'])
def handle_id(message: telebot.types.Message):
    from pprint import pprint
    pprint(message.json)


if __name__ == '__main__':
    load_config()
    bot.polling(none_stop=False, interval=0, timeout=20)
