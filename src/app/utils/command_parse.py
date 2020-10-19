

def parse_new_group(text):
    text_a = text.split()
    if not text_a or len(text_a) != 2:
        return None
    group_name = text_a[1]
    return group_name
