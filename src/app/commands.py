from datetime import datetime

from pymongo.database import Database
from telebot.types import Message

from app.db import DBS
from app.settings.consts import SUCCESSED_TEXT, ERROR_PARSE_MESSAGE, TABLE_URL
from app.utils.command_parse import parse_new_group
from app.utils.gtables import parse_gtable


def new_group_command(message: Message):
    group_name = parse_new_group(message.text)
    if not group_name:
        return ERROR_PARSE_MESSAGE

    db: Database = DBS['mongo']['client']

    db.get_collection('users').update_one({
        '_id': message.from_user.id
    }, {
        '$set': {'user_table': group_name}
    }, upsert=False)

    db.get_collection('users_tables').insert_one({
        '_id': group_name,
        'user_id': message.from_user.id,
        'lesson_date': datetime.now(),
    })
    parse_gtable(TABLE_URL)
    return SUCCESSED_TEXT


def start_lesson_command(message: Message):
    db: Database = DBS['mongo']['client']
    user = db.get_collection('users').find_one({
        '_id': message.from_user.id
    })
    user_table = user['user_table']

    # db.get_collection('users_tables').update_one({
    #     '_id': user_table,
    #     'user_id': message.from_user.id,
    # }, {'$set': {
    #     'table_content': {"push": }
    # }})
    return SUCCESSED_TEXT
