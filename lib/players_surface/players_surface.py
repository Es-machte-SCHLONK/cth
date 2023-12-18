import pygame as pyg


class Players:
    def __init__(self, root_screen):
        self.color = (0, 100, 0)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.init_surface()

    def init_surface(self):
        self.surface = pyg.Surface(
            (
                int(self.root_width * 0.5), (self.root_height - int(self.root_height * 0.8))
            )
        )
        self.surface.fill(self.color)
