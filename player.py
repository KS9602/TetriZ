class Player:

    """Simple player class"""

    def __init__(self) -> None:
        self._nick = "nick"

    @property
    def nick(self) -> str:
        return self._nick

    @nick.getter
    def nick(self) -> str:
        return self._nick

    @nick.setter
    def nick(self, value) -> None:
        if isinstance(value, str):
            self._nick = value
        else:
            raise TypeError

