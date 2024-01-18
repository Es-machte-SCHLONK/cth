# Class for Player Management

class Playermanagement:
    def __init__(self):
        self._active_player = ""

    @property
    def active_player(self):
        return self._active_player

    @active_player.setter
    def active_player(self, value):
        self._active_player = value
