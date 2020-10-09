from app.command_processor import CommandProcessor
from app.commands import add_command, AbstractCommand
from app.keyboard import use_keyboard, KEYBOARDS_PROCESSORS


@add_command('/test')
class TestCommand(AbstractCommand):
    def __init__(self, cmd_p: CommandProcessor):
        super().__init__(cmd_p)
        self = use_keyboard('test')(self)

    def do_command(self) -> None:
        self.response = self.cmd_p._command_args
