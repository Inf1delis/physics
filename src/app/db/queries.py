# It's a file where you can store your queries to the database
# For example,
# QUERY_ORDER_DATA = (
#     "SELECT t1.a, t2.b FROM database.table1 as t1"
#     " LEFT JOIN database.table2 as t2 on t1.a = t2.b "
#     " WHERE t1.robot <> 3 AND t2.b = :injected_param"
# )
from datetime import datetime


def UPDATE_USER_GROUP(user_id, group_name):
    return ({
        '_id': user_id
    }, {
        '$set': {
            '_id': user_id,
            'user_table': group_name
        }
    })


def START_GROUP_LESSON(user_id, group_name):
    return ({
        '_id': group_name,
        'user_id': user_id
    }, {
        '$set': {
            'lesson_date': datetime.now(),
        }
    })


def GET_USER_BY_ID(user_id):
    return [{
        '$lookup': {
            'from': "users_tables",
            'localField': "user_table",
            'foreignField': "_id",
            'as': 'merge'
        }}, {
        '$project': {
            'table': { '$arrayElemAt': [ "$merge", 0 ] },
            'user_table': 1
            }
        }, {
        '$match': { '_id': user_id }
        }
    ]
