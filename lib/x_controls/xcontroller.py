import random

import pygame as pyg


class XController:
    def __init__(self):
        self.player_positions = None
        self.x_position = None

    def set_x_position(self, x_position):
        self.x_position = x_position

    def get_player_position(self, player_position):
        self.player_positions = player_position

    def estimate_move(self, neighbor):
        # get neighbor nodes of actual position --> Muss in Main passieren
        # get position muss vorher passieren
        # check if occupied by players
        for point in neighbor:
            if point in self.player_positions:
                neighbor.remove(point)
        # random move
        rnd_turn = random.randint(0, len(neighbor))

        # publish move
        self.x_position = rnd_turn
        return neighbor[rnd_turn]

