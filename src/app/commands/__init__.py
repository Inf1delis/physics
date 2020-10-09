# Here you can store your commands
from dataclasses import dataclass
from typing import Dict

from app.command_processor import CommandProcessor
from app.keyboard import AbstractKeyboardProcessor


@dataclass(init=True)
class AbstractCommand:
    cmd_p: CommandProcessor
    response = None
    kbrd_process = AbstractKeyboardProcessor

    def __post_init__(self):
        self.kbrd_process = AbstractKeyboardProcessor() # type: AbstractKeyboardProcessor

    def do_command(self) -> None:
        pass

    def do_keyboard(self) -> None:
        self.response = self.kbrd_process.modify_message(self.cmd_p, self.response)


COMMANDS: Dict[str, AbstractCommand] = {}


def add_command(command: str):
    def _add_command(_class: AbstractCommand):
        COMMANDS[command] = _class
        return _class
    return _add_command


def init_commands():
    import app.commands.commands

init_commands()