import math
from math import floor

import pygame as pyg

"""
SORRY, 2 Tage dran gesessen eine dynamische Karte zu erstellen und auswertbar zu machen.
Letztendlich hat die Erstellung zwar geklappt, die Spielbarkeit konnte aber nicht garantiert werden.
Daher habe ich aufgegeben und mit viel Pfusch die Map statisch gecoded.
"""


class Node:
    def __init__(self):
        self.number = None
        self.position = None
        self.red = False
        self.green = False
        self.yellow = False
        self.color = (255, 255, 255)
        self.neighbours = []

    def set_color(self):
        if self.red:
            self.color = (255, 107, 97)
        elif self.green:
            self.color = (66, 219, 73)
        elif self.yellow:
            self.color = (255, 250, 97)

    def set_neighbour(self, neighbour_node):
        self.neighbours.append(neighbour_node)
        neighbour_node.neighbours.append(self)


class Map:
    def __init__(self, root_screen):
        self.map_color = (34, 34, 34)
        self.surface = self.init_surface(root_screen)
        self.red_nodes = []
        self.green_nodes = []
        self.yellow_nodes = []
        self.node_positions = dict()
        self.node_count = 0

        self.add_red_nodes()
        self.add_green_nodes()
        self.add_yellow_nodes()
        self.add_neighbours()

        self.draw_edges()
        self.draw_nodes()

        # print(self.node_positions.keys())

    def init_surface(self, root_screen):
        surface = pyg.Surface((root_screen.get_width(), (int(root_screen.get_height() * 0.8))))
        surface.fill(self.map_color)
        return surface

    def get_distance(self, pos_xy_1, pos_xy_2):
        x1, y1 = pos_xy_1
        x2, y2 = pos_xy_2
        distance = math.sqrt((x2 - x1) ** 2 + (y2 - y1) ** 2)
        return distance

    def select_node(self, position):
        selected_node = self.node_positions[position]
        self.draw_nodes()
        font = pyg.font.SysFont("arial bold", 16)

        number = font.render(str(selected_node.number), True, selected_node.color)
        pyg.draw.circle(self.surface, (2, 18, 115), selected_node.position, 10)
        self.surface.blit(number, number.get_rect(center=selected_node.position))

    def set_player_position(self, old_position, new_position, player_color=(255, 61, 242)):
        selected_node = self.node_positions[new_position]
        pyg.draw.circle(self.surface, player_color, selected_node.position, 20)
        pyg.draw.circle(self.surface, self.map_color, old_position, 25)
        self.draw_nodes()

    def select_edge(self, pos_start, pos_end):
        source_node = self.node_positions[pos_start]
        pos_end_neighbour = -1
        for i in range(0, len(source_node.neighbours)):
            if source_node.neighbours[i].position == pos_end:
                pos_end_neighbour = i

        if pos_end_neighbour >= 0:
            destination_node = source_node.neighbours[pos_end_neighbour]
            self.draw_edges()
            pyg.draw.line(self.surface, (2, 18, 115), source_node.position, destination_node.position, 2)
            self.select_node(destination_node.position)
        else:
            print("pos_end: " + str(pos_end))
            print("selected node neighbours: " + str(source_node.neighbours))
            print("Node not in reach! Select another node in with direct connection!")

    def add_red_nodes(self):
        # red_node northwest
        red1_1 = Node()
        red1_1.position = (30, 30)
        red1_1.red = True
        # red_node north
        red2_1 = Node()
        red2_1.position = (floor(self.surface.get_width() / 2), 30)
        red2_1.red = True
        # red_node northeast
        red3_1 = Node()
        red3_1.position = (self.surface.get_width() - 30, 30)
        red3_1.red = True

        # red_node southwest
        red1_2 = Node()
        red1_2.position = (30, self.surface.get_height() - 30)
        red1_2.red = True
        # red_node south
        red2_2 = Node()
        red2_2.position = (floor(self.surface.get_width() / 2), self.surface.get_height() - 30)
        red2_2.red = True
        # red_node southeast
        red3_2 = Node()
        red3_2.position = (self.surface.get_width() - 30, self.surface.get_height() - 30)
        red3_2.red = True

        # add to nodes.
        self.red_nodes.append(red1_1)  # 0
        self.node_positions[self.red_nodes[0].position] = self.red_nodes[0]
        self.node_count += 1
        self.red_nodes[0].number = self.node_count
        self.red_nodes.append(red2_1)  # 1
        self.node_positions[self.red_nodes[1].position] = self.red_nodes[1]
        self.node_count += 1
        self.red_nodes[1].number = self.node_count
        self.red_nodes.append(red3_1)  # 2
        self.node_positions[self.red_nodes[2].position] = self.red_nodes[2]
        self.node_count += 1
        self.red_nodes[2].number = self.node_count
        self.red_nodes.append(red1_2)  # 3
        self.node_positions[self.red_nodes[3].position] = self.red_nodes[3]
        self.node_count += 1
        self.red_nodes[3].number = self.node_count
        self.red_nodes.append(red2_2)  # 4
        self.node_positions[self.red_nodes[4].position] = self.red_nodes[4]
        self.node_count += 1
        self.red_nodes[4].number = self.node_count
        self.red_nodes.append(red3_2)  # 5
        self.node_positions[self.red_nodes[5].position] = self.red_nodes[5]
        self.node_count += 1
        self.red_nodes[5].number = self.node_count

        for n in self.red_nodes:
            n.set_color()

    def add_green_nodes(self):
        green_x_distance = floor(self.surface.get_width() / 6)
        green_y_distance = floor(self.surface.get_height() / 6)

        # left col 1
        green_node_1 = Node()
        green_node_1.position = (1 * green_x_distance, 3 * green_y_distance)
        green_node_1.green = True

        # left col 2 (2x)
        green_node_2 = Node()
        green_node_2.position = (2 * green_x_distance, 1 * green_y_distance)
        green_node_2.green = True

        green_node_3 = Node()
        green_node_3.position = (2 * green_x_distance, 5 * green_y_distance)
        green_node_3.green = True

        # left col 3 (2x)
        green_node_4 = Node()
        green_node_4.position = (3 * green_x_distance, 2 * green_y_distance)
        green_node_4.green = True

        green_node_5 = Node()
        green_node_5.position = (3 * green_x_distance, 4 * green_y_distance)
        green_node_5.green = True

        # left col 4 (2x)
        green_node_6 = Node()
        green_node_6.position = (4 * green_x_distance, 1 * green_y_distance)
        green_node_6.green = True

        green_node_7 = Node()
        green_node_7.position = (4 * green_x_distance, 5 * green_y_distance)
        green_node_7.green = True

        # left col 5 (1x)
        green_node_8 = Node()
        green_node_8.position = (5 * green_x_distance, 3 * green_y_distance)
        green_node_8.green = True

        self.green_nodes.append(green_node_1)
        self.node_positions[self.green_nodes[0].position] = self.green_nodes[0]
        self.node_count += 1
        self.green_nodes[0].number = self.node_count
        self.green_nodes.append(green_node_2)
        self.node_positions[self.green_nodes[1].position] = self.green_nodes[1]
        self.node_count += 1
        self.green_nodes[1].number = self.node_count
        self.green_nodes.append(green_node_3)
        self.node_positions[self.green_nodes[2].position] = self.green_nodes[2]
        self.node_count += 1
        self.green_nodes[2].number = self.node_count
        self.green_nodes.append(green_node_4)
        self.node_positions[self.green_nodes[3].position] = self.green_nodes[3]
        self.node_count += 1
        self.green_nodes[3].number = self.node_count
        self.green_nodes.append(green_node_5)
        self.node_positions[self.green_nodes[4].position] = self.green_nodes[4]
        self.node_count += 1
        self.green_nodes[4].number = self.node_count
        self.green_nodes.append(green_node_6)
        self.node_positions[self.green_nodes[5].position] = self.green_nodes[5]
        self.node_count += 1
        self.green_nodes[5].number = self.node_count
        self.green_nodes.append(green_node_7)
        self.node_positions[self.green_nodes[6].position] = self.green_nodes[6]
        self.node_count += 1
        self.green_nodes[6].number = self.node_count
        self.green_nodes.append(green_node_8)
        self.node_positions[self.green_nodes[7].position] = self.green_nodes[7]
        self.node_count += 1
        self.green_nodes[7].number = self.node_count
        for n in self.green_nodes:
            n.set_color()

    def add_yellow_nodes(self):
        col_width = floor(self.surface.get_width() / 12)
        row_height = floor(self.surface.get_height() / 12)

        def yellow_node(count_i, count_j):
            node = Node()
            node.position = ((count_i + 1) * col_width, (count_j + 1) * row_height - 51)
            node.yellow = True
            self.node_count += 1
            node.number = self.node_count
            node.set_color()
            self.yellow_nodes.append(node)
            self.node_positions[node.position] = node

        # generate nodes with randomized location
        for i in range(0, 12):
            for j in range(0, 12):

                if (i == 0 and j == 4) or (i == 0 and j == 6) or (i == 0 and j == 8) or (
                        i == 10 and j == 4) or (i == 10 and j == 6) or (i == 10 and j == 8):
                    yellow_node(i, j)
                if (i == 1 and j == 2) or (i == 1 and j == 4) or (i == 1 and j == 8) or (i == 1 and j == 10) or (
                        i == 9 and j == 2) or (i == 9 and j == 4) or (i == 9 and j == 8) or (i == 9 and j == 10):
                    yellow_node(i, j)
                if (i == 2 and j == 3) or (i == 2 and j == 5) or (i == 2 and j == 7) or (i == 2 and j == 9) or (
                        i == 8 and j == 3) or (i == 8 and j == 5) or (i == 8 and j == 7) or (i == 8 and j == 9):
                    yellow_node(i, j)
                if (i == 3 and j == 4) or (i == 3 and j == 6) or (i == 3 and j == 8) or (
                        i == 7 and j == 4) or (i == 7 and j == 6) or (i == 7 and j == 8):
                    yellow_node(i, j)
                if (i == 4 and j == 2) or (i == 4 and j == 5) or (i == 4 and j == 7) or (i == 4 and j == 10) or (
                        i == 6 and j == 2) or (i == 6 and j == 5) or (i == 6 and j == 7) or (i == 6 and j == 10):
                    yellow_node(i, j)
                # center!
                if (i == 5 and j == 3) or (i == 5 and j == 9):
                    yellow_node(i, j)

        self.yellow_nodes[1].set_neighbour(self.yellow_nodes[0])
        self.yellow_nodes[1].set_neighbour(self.yellow_nodes[2])
        self.yellow_nodes[1].set_neighbour(self.green_nodes[0])
        self.yellow_nodes[3].set_neighbour(self.yellow_nodes[0])
        self.yellow_nodes[3].set_neighbour(self.yellow_nodes[4])
        self.yellow_nodes[3].set_neighbour(self.red_nodes[0])
        self.yellow_nodes[4].set_neighbour(self.yellow_nodes[0])
        self.yellow_nodes[5].set_neighbour(self.yellow_nodes[2])
        self.yellow_nodes[5].set_neighbour(self.yellow_nodes[6])
        self.yellow_nodes[6].set_neighbour(self.yellow_nodes[2])
        self.yellow_nodes[6].set_neighbour(self.yellow_nodes[2])
        self.yellow_nodes[6].set_neighbour(self.yellow_nodes[2])
        self.yellow_nodes[6].set_neighbour(self.red_nodes[3])
        self.yellow_nodes[7].set_neighbour(self.yellow_nodes[3])
        self.yellow_nodes[7].set_neighbour(self.yellow_nodes[4])
        self.yellow_nodes[7].set_neighbour(self.yellow_nodes[8])
        self.yellow_nodes[7].set_neighbour(self.green_nodes[1])
        self.yellow_nodes[8].set_neighbour(self.yellow_nodes[4])
        self.yellow_nodes[8].set_neighbour(self.yellow_nodes[9])
        self.yellow_nodes[8].set_neighbour(self.green_nodes[0])
        self.yellow_nodes[9].set_neighbour(self.yellow_nodes[5])
        self.yellow_nodes[9].set_neighbour(self.yellow_nodes[10])
        self.yellow_nodes[9].set_neighbour(self.green_nodes[0])
        self.yellow_nodes[10].set_neighbour(self.yellow_nodes[5])
        self.yellow_nodes[10].set_neighbour(self.yellow_nodes[6])
        self.yellow_nodes[10].set_neighbour(self.green_nodes[2])
        self.yellow_nodes[11].set_neighbour(self.yellow_nodes[8])
        self.yellow_nodes[11].set_neighbour(self.yellow_nodes[12])
        self.yellow_nodes[12].set_neighbour(self.yellow_nodes[8])
        self.yellow_nodes[12].set_neighbour(self.yellow_nodes[9])
        self.yellow_nodes[12].set_neighbour(self.yellow_nodes[13])
        self.yellow_nodes[13].set_neighbour(self.yellow_nodes[9])
        self.yellow_nodes[14].set_neighbour(self.green_nodes[1])
        self.yellow_nodes[14].set_neighbour(self.red_nodes[1])
        self.yellow_nodes[15].set_neighbour(self.yellow_nodes[11])
        self.yellow_nodes[15].set_neighbour(self.yellow_nodes[12])
        self.yellow_nodes[15].set_neighbour(self.yellow_nodes[16])
        self.yellow_nodes[15].set_neighbour(self.green_nodes[3])
        self.yellow_nodes[16].set_neighbour(self.yellow_nodes[12])
        self.yellow_nodes[16].set_neighbour(self.yellow_nodes[13])
        self.yellow_nodes[16].set_neighbour(self.green_nodes[4])
        self.yellow_nodes[17].set_neighbour(self.green_nodes[2])
        self.yellow_nodes[17].set_neighbour(self.red_nodes[4])
        self.yellow_nodes[18].set_neighbour(self.yellow_nodes[14])
        self.yellow_nodes[18].set_neighbour(self.green_nodes[3])
        self.yellow_nodes[19].set_neighbour(self.yellow_nodes[17])
        self.yellow_nodes[19].set_neighbour(self.green_nodes[4])
        self.yellow_nodes[20].set_neighbour(self.yellow_nodes[14])
        self.yellow_nodes[20].set_neighbour(self.yellow_nodes[18])
        self.yellow_nodes[20].set_neighbour(self.green_nodes[5])
        self.yellow_nodes[20].set_neighbour(self.red_nodes[1])
        self.yellow_nodes[21].set_neighbour(self.yellow_nodes[22])
        self.yellow_nodes[21].set_neighbour(self.green_nodes[3])
        self.yellow_nodes[22].set_neighbour(self.green_nodes[4])
        self.yellow_nodes[23].set_neighbour(self.yellow_nodes[17])
        self.yellow_nodes[23].set_neighbour(self.yellow_nodes[19])
        self.yellow_nodes[23].set_neighbour(self.green_nodes[6])
        self.yellow_nodes[23].set_neighbour(self.red_nodes[4])
        self.yellow_nodes[24].set_neighbour(self.yellow_nodes[21])
        self.yellow_nodes[24].set_neighbour(self.yellow_nodes[25])
        self.yellow_nodes[25].set_neighbour(self.yellow_nodes[21])
        self.yellow_nodes[25].set_neighbour(self.yellow_nodes[22])
        self.yellow_nodes[25].set_neighbour(self.yellow_nodes[26])
        self.yellow_nodes[26].set_neighbour(self.yellow_nodes[22])
        self.yellow_nodes[27].set_neighbour(self.yellow_nodes[28])
        self.yellow_nodes[27].set_neighbour(self.green_nodes[5])
        self.yellow_nodes[28].set_neighbour(self.yellow_nodes[24])
        self.yellow_nodes[28].set_neighbour(self.yellow_nodes[25])
        self.yellow_nodes[28].set_neighbour(self.yellow_nodes[29])
        self.yellow_nodes[28].set_neighbour(self.green_nodes[7])
        self.yellow_nodes[29].set_neighbour(self.yellow_nodes[25])
        self.yellow_nodes[29].set_neighbour(self.yellow_nodes[26])
        self.yellow_nodes[29].set_neighbour(self.yellow_nodes[30])
        self.yellow_nodes[29].set_neighbour(self.green_nodes[7])
        self.yellow_nodes[30].set_neighbour(self.green_nodes[6])
        self.yellow_nodes[31].set_neighbour(self.yellow_nodes[27])
        self.yellow_nodes[31].set_neighbour(self.yellow_nodes[32])
        self.yellow_nodes[31].set_neighbour(self.red_nodes[2])
        self.yellow_nodes[32].set_neighbour(self.yellow_nodes[27])
        self.yellow_nodes[32].set_neighbour(self.yellow_nodes[28])
        self.yellow_nodes[33].set_neighbour(self.yellow_nodes[29])
        self.yellow_nodes[33].set_neighbour(self.yellow_nodes[30])
        self.yellow_nodes[33].set_neighbour(self.yellow_nodes[34])
        self.yellow_nodes[34].set_neighbour(self.yellow_nodes[30])
        self.yellow_nodes[34].set_neighbour(self.red_nodes[5])
        self.yellow_nodes[35].set_neighbour(self.yellow_nodes[31])
        self.yellow_nodes[35].set_neighbour(self.yellow_nodes[32])
        self.yellow_nodes[35].set_neighbour(self.yellow_nodes[36])
        self.yellow_nodes[36].set_neighbour(self.yellow_nodes[37])
        self.yellow_nodes[36].set_neighbour(self.green_nodes[7])
        self.yellow_nodes[37].set_neighbour(self.yellow_nodes[33])
        self.yellow_nodes[37].set_neighbour(self.yellow_nodes[34])

    def add_neighbours(self):
        self.red_nodes[0].set_neighbour(self.red_nodes[1])
        self.red_nodes[0].set_neighbour(self.red_nodes[3])
        self.red_nodes[0].set_neighbour(self.green_nodes[0])
        self.red_nodes[0].set_neighbour(self.green_nodes[1])

        self.red_nodes[1].set_neighbour(self.red_nodes[2])
        self.red_nodes[1].set_neighbour(self.green_nodes[1])
        self.red_nodes[1].set_neighbour(self.green_nodes[5])

        self.red_nodes[2].set_neighbour(self.red_nodes[5])
        self.red_nodes[2].set_neighbour(self.green_nodes[5])
        self.red_nodes[2].set_neighbour(self.green_nodes[7])

        self.red_nodes[3].set_neighbour(self.red_nodes[4])
        self.red_nodes[3].set_neighbour(self.green_nodes[0])
        self.red_nodes[3].set_neighbour(self.green_nodes[2])

        self.red_nodes[4].set_neighbour(self.red_nodes[5])
        self.red_nodes[4].set_neighbour(self.green_nodes[2])
        self.red_nodes[4].set_neighbour(self.green_nodes[6])

        self.red_nodes[5].set_neighbour(self.green_nodes[6])
        self.red_nodes[5].set_neighbour(self.green_nodes[7])

        self.green_nodes[0].set_neighbour(self.green_nodes[1])
        self.green_nodes[0].set_neighbour(self.green_nodes[2])

        self.green_nodes[1].set_neighbour(self.green_nodes[3])

        self.green_nodes[2].set_neighbour(self.green_nodes[4])

        self.green_nodes[3].set_neighbour(self.green_nodes[4])
        self.green_nodes[3].set_neighbour(self.green_nodes[5])

        self.green_nodes[4].set_neighbour(self.green_nodes[6])

        self.green_nodes[5].set_neighbour(self.green_nodes[7])

        self.green_nodes[6].set_neighbour(self.green_nodes[7])

    def draw_nodes(self):
        font = pyg.font.SysFont("arial bold", 16)
        for n in self.red_nodes:
            number = font.render(str(n.number), True, (0, 0, 0))
            pyg.draw.circle(self.surface, n.color, n.position, 10)
            self.surface.blit(number, number.get_rect(center=n.position))
        for n in self.green_nodes:
            number = font.render(str(n.number), True, (0, 0, 0))
            pyg.draw.circle(self.surface, n.color, n.position, 10)
            self.surface.blit(number, number.get_rect(center=n.position))
        for n in self.yellow_nodes:
            number = font.render(str(n.number), True, (0, 0, 0))
            pyg.draw.circle(self.surface, n.color, n.position, 10)
            self.surface.blit(number, number.get_rect(center=n.position))

    def draw_edges(self):

        for n in self.yellow_nodes:
            edge_color = n.color
            for nb in n.neighbours:
                pyg.draw.line(self.surface, edge_color, n.position, nb.position, 2)

        for n in self.green_nodes:
            for nb in n.neighbours:
                if nb.yellow:
                    edge_color = nb.color
                else:
                    edge_color = n.color
                pyg.draw.line(self.surface, edge_color, n.position, nb.position, 2)
        for n in self.red_nodes:
            for nb in n.neighbours:
                if nb.green | nb.yellow:
                    edge_color = nb.color
                else:
                    edge_color = n.color
                pyg.draw.line(self.surface, edge_color, n.position, nb.position, 2)
