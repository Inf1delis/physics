import pytest

from app.command_processor import CommandProcessor


# TODO rewite tests
def test_command_processor():
    cmd_p = CommandProcessor(1, 1, '/test test string with cmd')
    print(cmd_p.do_action())
    cmd_p = CommandProcessor(1, 1, 'test string with no cmd')
    print(cmd_p.do_action())