from dataclasses import dataclass


@dataclass
class TelegramHandler:
    request = None
    responce = None

    def __post_init__(self):
        self._parse_request()
        self._get_keyboard()

    def _parse_request(self):
        pass

    def _get_keyboard(self):
        pass

    def do(self) -> None:
        pass
