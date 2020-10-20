from telebot.types import InlineKeyboardMarkup, InlineKeyboardButton


def keyboard_builder(name):
    """
    Формирование кнопочек
    :return:
    """
    scores = ['0.25', '0.5', '1']
    scores_btn = []
    for score in scores:
        callback_data = '{}${}'.format(name, score)
        btn = InlineKeyboardButton(text=score, callback_data=callback_data)
        scores_btn += [btn]

    reply_key_board = InlineKeyboardMarkup()
    reply_key_board.row(*scores_btn)
    return reply_key_board
