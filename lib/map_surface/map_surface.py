import pygame as pyg
from lib.map_surface import nodelist as nl

#hallo
class Maps:
    def __init__(self, root_screen):
        self.map_color = (34, 34, 34)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.init_surface()

    def init_surface(self):
        self.surface = pyg.Surface((self.root_width, (int(self.root_height * 0.8))))
        self.surface.fill(self.map_color)
        nodelist = nl.NodeList(10)
        nodelist.draw_node(self.surface)
