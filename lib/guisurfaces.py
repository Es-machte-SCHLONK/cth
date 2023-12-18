import pygame as pyg
from cth.lib import graph as map


class GuiSurfaces:
    def __init__(self, root_screen):
        self.map_surface = None
        self.players_surface = None
        self.actions_surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        # 1. map, 2. players, 3. actions!
        self.init_map_surfaces()
        self.init_players_surfaces()
        self.init_actions_surfaces()

    def init_map_surfaces(self):
        map_height = int(self.root_height * 0.8)
        map_color = (34, 34, 34)
        self.map_surface = pyg.Surface((self.root_width, map_height))
        self.map_surface.fill(map_color)

    def init_players_surfaces(self):
        players_height = self.root_height - self.map_surface.get_height()
        players_width = int(self.root_width * 0.5)
        players_color = (0, 100, 0)
        self.players_surface = pyg.Surface((players_width, players_height))
        self.players_surface.fill(players_color)

    def init_actions_surfaces(self):
        actions_height = self.players_surface.get_height()
        actions_width = self.root_width - self.players_surface.get_width()
        actions_color = (138, 0, 0)
        self.actions_surface = pyg.Surface((actions_width, actions_height))
        self.actions_surface.fill(actions_color)

    def draw_map_surface(self, node_count):
        graph = map.Graph(node_count)
        graph.draw_graph(self.map_surface)

