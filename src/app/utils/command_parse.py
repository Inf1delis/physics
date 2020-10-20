def _parse_one_arg(text):
    args_array = text.strip().split()
    if not args_array or len(args_array) != 2:
        return None
    arg = args_array[1]
    return arg


def parse_group_name(text):
    return _parse_one_arg(text)


def parse_student_substring(text):
    return _parse_one_arg(text)

def parse_name_and_score(text):
    """
        Парсинг строки для получения имени студента и его баллов
    :return:
    """
    args_array = text.strip().split('$')
    if not args_array or len(args_array) != 2:
        return None, None
    return args_array[0], float(args_array[1])