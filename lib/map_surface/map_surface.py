import pygame as pyg
from cth.lib.map_surface import nodelist as nl

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

    def draw_map_surface(self, node_count):
        self.init_surface()
        self.graph.nodeList.nodes.clear()
        node_count = self.graph.get_node_count()
        print("Drawing map with "+str(node_count)+" Nodes.")
        self.graph.draw_graph(self.surface)