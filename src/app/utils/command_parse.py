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
