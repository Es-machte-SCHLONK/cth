import sys

import pygame as pyg

from lib.players_surface.Player import Player


class PlayerUI:

    def __init__(self, root_screen):
        self.color = (0, 100, 0)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.init_surface()
        self.players = []
        self.player_rect_size = 50

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
        # Hier zeichnest du die Spieler auf das Fenster
        if self.players:
            player_rect_x = 50
            player_rect_y = 50

            for player in self.players:
                pyg.draw.rect(self.surface, player.color, (player_rect_x, player_rect_y, self.player_rect_size,
                                                           self.player_rect_size))
                player_rect_x += 100  # Abstand zwischen den Spieler-Rechtecken

    # In main ?


if __name__ == "__main__":
    player_ui = PlayerUI()
    player_ui.add_player("Player 1", (255, 0, 0))
    player_ui.add_player("Player 2", (0, 255, 0))
    player_ui.add_player("Player 3", (0, 0, 255))
