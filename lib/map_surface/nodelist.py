import random
import datetime
import pygame as pyg
from cth.lib.map_surface import nodes


class NodeList:
    now = float(datetime.datetime.now().timestamp())
    random.seed(now)
    nodes = []

    # Additional Information, based on official Scotland Yard lib:
    #   every 3.333 nodes, a GREEN node.    >> 30 per 100  >> 300 per 1000
    #   every 13.333 nodes, a RED node.     >> 7,5 per 100 >> 75 per 1000
    #   every 40 nodes, a BLACK node.       >> 2,5 per 100 >> 25 per 1000
    #   Every RED node is also GREEN and YELLOW node.
    #   Black nodes are special.
    def __init__(self, node_count):
        self.green_count = 0
        self.red_count = 0
        self.black_count = 0
        for i in range(1, node_count + 1):
            random_int_color = random.randint(1, 1000)
            random_int_black = random.randint(1, 1000)
            if random_int_color <= 75:
                new_node = nodes.Node(i, True, True)
                self.green_count += 1
                self.red_count += 1
            elif random_int_color <= 300:
                new_node = nodes.Node(i, True, False)
                self.red_count += 1
            else:
                new_node = nodes.Node(i, False, False)

            if random_int_black <= 25:
                new_node.set_black()
                self.black_count += 1

            self.nodes.append(new_node)

    def __str__(self):
        strings = []
        for node in self.nodes:
            string = str(node)
            strings.append(string)
        total = str(
            f"\n"
            f"Overview:\n"
            f"\tYellow Nodes: {len(self.nodes)}\n"
            f"\tGreen Nodes: {str(self.green_count)}\n"
            f"\tRed Nodes: {str(self.red_count)}\n"
            f"\tBlack Nodes: {str(self.black_count)}\n"
        )
        print_string = "\n".join(strings)
        print_string = print_string.join(total)
        return print_string

    def draw_graph(self, map_surface):
        yellow_color = (200, 150, 0)
        green_color = (0, 100, 0)
        red_color = (100, 0, 0)
        black_color = (128, 128, 128)
        node_color = black_color
        for node in self.nodes:
            x = random.randint(0 + node.node_size, map_surface.get_width() - node.node_size)
            y = random.randint(0 + node.node_size, map_surface.get_height() - node.node_size)
            if node.yellow:
                node_color = yellow_color
            if node.green:
                node_color = green_color
            if node.red:
                node_color = red_color
            pyg.draw.circle(map_surface, node_color, (x, y), node.node_size)

    def get_node_count(self):
        return len(self.nodes)
