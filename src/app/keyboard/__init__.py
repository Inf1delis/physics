# Here you can store your commands
from typing import Dict

from app.command_processor import CommandProcessor


class AbstractKeyboardProcessor:

    def modify_message(self, cmd_p: CommandProcessor, response) -> str:
        return response


KEYBOARDS_PROCESSORS: Dict[str, AbstractKeyboardProcessor] = {}


def use_keyboard(kbrd_name: str):
    def _add_command(_class):
        _class.kbrd_process = KEYBOARDS_PROCESSORS[kbrd_name]
        return _class

    return _add_command


def add_keyboard(kbrd_name: str):
    def _add_command(kbrd: AbstractKeyboardProcessor):
        KEYBOARDS_PROCESSORS[kbrd_name] = kbrd()
        return kbrd

    return _add_command


def init_keyboards():
    import app.keyboard.keyboards


init_keyboards()
