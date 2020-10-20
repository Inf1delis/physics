from pygsheets import WorksheetNotFound
from pymongo.database import Database
from telebot.types import Message
import pandas as pd

from app.db import DBS
from app.db.queries import UPDATE_USER_GROUP, START_GROUP_LESSON, GET_USER_BY_ID
from app.settings import CONFIG
from app.settings.consts import SUCCESSED_TEXT, ERROR_PARSE_MESSAGE, SEARCH_NOT_FOUND_TEXT, WORKSHEET_NOT_EXISTS, PUPIL_NOT_FOUND
from app.utils.command_parse import parse_group_name, parse_student_substring, parse_name_and_score


def start_lesson_command(message: Message):
    """
    Реализация начала урока
    :param message:
    :return:
    """
    user_table = parse_group_name(message.text)
    if not user_table:
        return ERROR_PARSE_MESSAGE

    db: Database = DBS['mongo']['client']

    db.get_collection('users').update_one(
        *UPDATE_USER_GROUP(
            user_id=message.from_user.id,
            group_name=user_table),
        upsert=True)

    db.get_collection('users_tables').update_one(
        *START_GROUP_LESSON(
            user_id=message.from_user.id,
            group_name=user_table),
        upsert=True)

    return SUCCESSED_TEXT


def search_command(message: Message):
    """
    Реализация метода для поиска ученика
    :param message:
    :return:
    """
    student_substr = parse_student_substring(message.text)
    if not student_substr:
        return ERROR_PARSE_MESSAGE

    db: Database = DBS['mongo']['client']
    gtable = CONFIG['gtable']  # type: GTable

    user = get_user(message.from_user.id, db)
    user_table = user['user_table']
    try:
        df: pd.DataFrame = gtable.from_gsheet(user_table)
    except WorksheetNotFound:
        return WORKSHEET_NOT_EXISTS

    search = df.transpose().iloc[0].str.contains(student_substr, case=False)
    res_df = df[search]
    if res_df.empty:
        return SEARCH_NOT_FOUND_TEXT

    matched_students = df[search].transpose().iloc[0].values.tolist()

    #################################################
    ####### пример кода, как можно давать баллы людям
    #################################################
    # gtable.score_student(
    #     group_name=user_table,
    #     student_name=matched_students[0],
    #     score=0.1,
    #     lesson_date=user['table']['lesson_date'])
    #################################################
    return matched_students


def score_command(user_id, text):
    """
    Метод добавления оценки
    :param user_id:
    :param text:
    :return:
    """
    db: Database = DBS['mongo']['client']
    gtable = CONFIG['gtable']  # type: GTable

    user = get_user(user_id, db)
    if user is None or not user:
        return PUPIL_NOT_FOUND

    user_name, score = parse_name_and_score(text)

    gtable.score_student(
        group_name=user['user_table'],
        student_name=user_name,
        score=score,
        lesson_date=user['table']['lesson_date'])

    return f'Баллы в количестве={score} добавлены студенту {user_name}'


def get_user(user_id, db):
    """
    Получение идентификатора ученика для начисления баллов
    :return:
    """
    # этот метод возвращает список, пусть будет так, потом может исправим
    user_list = list(db.get_collection('users').aggregate(
        GET_USER_BY_ID(user_id=197079657)))

    if not user_list:
        return ERROR_PARSE_MESSAGE

    user = user_list[0]  # only one user
    return user
