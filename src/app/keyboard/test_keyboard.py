from app.command_processor import CommandProcessor
from app.keyboard import AbstractKeyboardProcessor, add_keyboard


@add_keyboard('test')
class TestKeyboard(AbstractKeyboardProcessor):

    def modify_message(self, cmd_p: CommandProcessor, response):
        response += ' keyboard'
        return response
