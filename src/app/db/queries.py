# It's a file where you can store your queries to the database
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
        '_id': '{}_{}'.format(user_id, group_name),
    }, {
        '$set': {
            'group_name': group_name,
            'user_id': user_id,
            'lesson_date': datetime.now(),
        }
    })


def GET_USER_BY_ID(user_id: int):
    return [{
        '$addFields': {
            'group_id': { '$concat': [ { "$toString": "$_id"}, "_", "$group_name" ] } }
        }, {
        '$lookup': {
            'from': "users_tables",
            'localField': "user_table",
            'foreignField': "group_name",
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
