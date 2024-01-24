import pygame as pyg

from lib.players_surface.Player import Player


class PlayerUI:

    def __init__(self, root_screen):
        self.color = (0, 100, 0)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.players = []
        self.players.append(Player("Hans", (150, 150, 150)))
        self.players.append(Player("Hilde", (150, 50, 200)))
        self.players.append(Player("Günther", (50, 150, 200)))
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
        if self.players:
            player_rect_x = 50
            player_rect_y = 60
            font = pyg.font.SysFont("arial bold", 18)
            for player in self.players:
                player_name = font.render(player.name, True, (0, 0, 0))

                pyg.draw.rect(self.surface, player.color, (player_rect_x, player_rect_y, self.player_rect_size,
                                                           self.player_rect_size))
                self.surface.blit(player_name, player_name.get_rect(topleft=(player_rect_x + 1, player_rect_y + 10)))
                player_rect_x += (30 + self.player_rect_size)  # Abstand zwischen den Spieler-Rechtecken"""
