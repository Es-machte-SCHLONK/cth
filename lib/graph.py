from cth.lib import nodelist as nl
import random
import datetime
import pygame as pyg


class Graph:

    def __init__(self, node_count):
        self.nodeList = nl.NodeList(node_count)

    def draw_graph(self, map_surface):
        now = float(datetime.datetime.now().timestamp())
        random.seed(now)
        yellow_color = (200, 150, 0)
        green_color = (0, 100, 0)
        red_color = (100, 0, 0)
        black_color = (128, 128, 128)
        node_color = black_color
        for node in self.nodeList.nodes:
            x = random.randint(0 + int(node.node_size % 2), map_surface.get_width())
            y = random.randint(0 + int(node.node_size % 2), map_surface.get_height())
            if node.yellow:
                node_color = yellow_color
            if node.green:
                node_color = green_color
            if node.red:
                node_color = red_color
            pyg.draw.circle(map_surface, node_color, (x, y), node.node_size)
