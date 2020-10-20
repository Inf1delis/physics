from pathlib import Path

from envparse import env

env.read_envfile()

DEBUG = env("DEBUG", default=False)

ROOT_DIR = Path(__name__).parent.parent
CONFIG_DIR = ROOT_DIR / "config"

VERSION = "2020.06.09"
SERVICE_NAME = "physics"

MSG_SERVICE_DESCRIPTION = "physics tg bot for a good mark"

TOKEN = env("BOT_TOKEN")

TABLE_URL = 'https://docs.google.com/spreadsheets/d/1dWyW47H6Qzk_k68ZHf7RXYc9-gq1FeXobWbp0iB5LmE/edit#gid=0'
TOTAL_DF_COL = 'Всего'

USER_ID = [
    197079657,  # Valya
    306633623  # Nikita
]

ERROR_PARSE_MESSAGE = 'Неправильное использование команды. Введите /help'
UNAUTHORIZED_USER_MESSAGE = 'Вы не добавили себе таблицу. /newGroup [group]'
SEARCH_NOT_FOUND_TEXT = 'По такой подстроке никого не найдено'
SUCCESSED_TEXT = 'Дело сделано'
WORKSHEET_NOT_EXISTS = 'Такого листа не существует в таблице. Пожалуйста, добавьте его сюда: {}'.format(TABLE_URL)

DICT_OF_BUTTONS = {1: 'Добавить баллы',
                   2: ['Добавить новый класс', 'Начать новый урок']}
GREETING_MESSAGE = 'Приветствуем вас в боте для выставления оценок, ' \
                   'созданном Валентином Мамедовым при поддержке Нелидова Никиты. Для знакомства напишите /help и ' \
                   'отправьте мне сообщение'
HELP_MESSAGE = 'Итак сейчас я расскажу вам о моем функционале. На данный момент вы видите перед собой две кнопки: ' \
               '"Добавить новый класс" и "Начать урок".' \
               'Первая команда - "Добавить новый класс" позволяет вам загрузить Google таблицу с ' \
               'Помимо тех команд, что вы видите на экране данный бот владеет следующими командами:' \
               '    1) /search: Данная команда позволяет произвести поиск нужного вам студента.' \
               '       Пример использования: /search Никита' \
               '       Данная команда выведет вам на экран всех пользователей с именем Никита'
