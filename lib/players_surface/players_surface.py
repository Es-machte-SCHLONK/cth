from math import floor

import pygame as pyg

from lib.players_surface.Player import Player


class PlayerUI:

    def __init__(self, root_screen):
        self.color = (0, 100, 0)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.players = []
        self.players.append(Player("Player 1", (218, 66, 245)))
        self.players.append(Player("Player 2", (66, 245, 194)))
        self.players.append(Player("Player 3", (245, 138, 66)))
        self.players.append(Player("Player 4", (217, 247, 119)))
        self.players.append(Player("Lady X", (191, 191, 191)))
        self.player_rect_size = 50
        self.init_surface()

    def init_surface(self):
        self.surface = pyg.Surface(
            (
                int(self.root_width * 0.5), (self.root_height - int(self.root_height * 0.8))
            )
        )
        self.update()
        self.surface.fill(self.color)
        # Spieler zeichnen
        self.draw_players()
        # Fenster aktualisieren
        pyg.display.flip()

    def add_player(self, name, color):
        new_player = Player(name, color)
        self.players.append(new_player)

    def update(self):
        # Hier könntest du die Spiellogik für die UI-Aktualisierung implementieren
        pass

    def draw_players(self):
        surface_width = self.surface.get_width()
        surface_height = self.surface.get_height()
        player_card_spacing = 15
        player_card_width = floor((surface_width - (6 * player_card_spacing)) / 5)
        player_card_height = floor(surface_height * 0.8)
        if self.players:
            player_rect_x = player_card_spacing
            font = pyg.font.SysFont("arial bold", 20)
            for player in self.players:
                player_name = font.render(player.name, True, (0, 0, 0))
                pyg.draw.rect(self.surface, (40, 40, 40),
                              (player_rect_x + 3, 15 + 3, player_card_width, player_card_height),
                              0, 10)
                pyg.draw.rect(self.surface, player.color, (player_rect_x, 15, player_card_width,
                                                           player_card_height), 0, 10)
                self.surface.blit(player_name, player_name.get_rect(center=(player_rect_x + (player_card_width//2), 30)))
                player_rect_x += (player_card_spacing + player_card_width)  # Abstand zwischen den Spieler-Rechtecken"""
