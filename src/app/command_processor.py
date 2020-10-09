from app.commands import *


@dataclass
class CommandProcessor:
    user_id: int
    message_id: int
    text: str
    _keyboard = None
    _command: str = None
    _command_args: str = None

    def __post_init__(self):
        self._parse_text()

    def _parse_text(self):
        splitted = self.text.split()
        self._cmd = splitted[0] if COMMANDS.get(splitted[0]) else '/test'
        self._command_args = ' '.join(splitted[1:])

    def do_action(self) -> str:
        Cmd = COMMANDS[self._cmd]
        cmd = Cmd(self)  # type: AbstractCommand
        cmd.do_command()
        print(cmd.kbrd_process)
        cmd.do_keyboard()
        return cmd.response
