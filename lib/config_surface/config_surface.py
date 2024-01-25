import pygame as pyg

from lib.players_surface.players_surface import PlayerUI
from main import Game

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class PlayerConfigUI:
    def __init__(self, root_screen):
        self.created_player = 0
        self.max_players = 4
        self.config_running = False

        # Fenstergröße und Farben
        self.surface = self.init_surface(root_screen)
        self.bg_color = (255, 255, 255)
        self.input_box_color = (200, 200, 200)
        self.font = pyg.font.Font(None, 32)
        self.clock = pyg.time.Clock()
        self.draw_menu()

    def init_surface(self, root_screen):
        surface = pyg.Surface((root_screen.get_width(), root_screen.get_height()))
        surface.fill((34, 34, 34))
        return surface

    def draw_menu(self):
        row_height = self.surface.get_height() / 6
        col_width = self.surface.get_width() / 6

        for i in range(0, 4):
            player_color = (255, 255, 255)
            if i == 0:
                player_color = (218, 66, 245)
            elif i == 1:
                player_color = (66, 245, 194)
            elif i == 2:
                player_color = (245, 138, 66)
            elif i == 3:
                player_color = (217, 247, 119)
            player_text = "Player " + str(i + 1)
            font = pyg.font.SysFont("arial bold", 32)
            player_label = font.render(player_text, True, player_color)
            self.surface.blit(player_label,
                              player_label.get_rect(topleft=(col_width, row_height * (i + 1))))
            instructions = "Enter player name or leave empty for no player"
            font = pyg.font.SysFont("arial bold", 16)
            instructions_label = font.render(instructions, True, (255, 255, 255))
            self.surface.blit(instructions_label,
                              instructions_label.get_rect(topleft=(col_width * 2, row_height * (i + 1) + 35)))
            pyg.draw.rect(self.surface, (255, 255, 255),
                          (col_width * 2, row_height * (i + 1) - 15, col_width * 2, player_label.get_height() * 2))
            pyg.draw.rect(self.surface, (80, 80, 80),
                          (col_width * 2, row_height * (i + 1) - 15, col_width * 2,
                           player_label.get_height() * 2), 2)
        pyg.draw.rect(self.surface, (10, 10, 10), (col_width * 1 + 3, row_height * 5 + 3, col_width * 3,
                                                   row_height * 0.5), 0, 10)
        pyg.draw.rect(self.surface, (0, 64, 19), (col_width * 1, row_height * 5, col_width * 3,
                                                  row_height * 0.5), 0, 10)
        pyg.draw.rect(self.surface, (9, 43, 19), (col_width * 1, row_height * 5, col_width * 3,
                                                  row_height * 0.5), 5, 10)
        pyg.draw.rect(self.surface, (11, 97, 36), (col_width * 1, row_height * 5, col_width * 3,
                                                   row_height * 0.5), 3, 10)
        button_text = "Let's play!"
        font = pyg.font.SysFont("arial bold", 48)
        button_label = font.render(button_text, True, (255, 255, 255))
        self.surface.blit(button_label,
                          button_label.get_rect(center=(col_width * 2.5, row_height * 5.25)))

    def leave_config(self):
        self.config_running = False
