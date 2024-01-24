import sys

import pygame as pyg

from lib.players_surface.Player import Player
from lib.players_surface.players_surface import PlayerUI



class PlayerConfigUI:
    def __init__(self):
        self.players = []
        self.selected_player = 1  # Spieler, der aktuell konfiguriert wird
        self.max_players = 4

        pyg.init()

        # Fenstergröße und Farben
        self.width, self.height = 800, 600
        self.bg_color = (255, 255, 255)
        self.input_box_color = (200, 200, 200)
        self.font = pyg.font.Font(None, 32)

        # Eingabevariablen für Name und Farbe
        self.player_name_input = ""
        self.player_color_input = (255, 0, 0)

        # SpielerUI-Instanz erstellen
        self.player_ui = PlayerUI(self.players)

        # Fenster erstellen
        self.screen = pyg.display.set_mode((self.width, self.height))
        pyg.display.set_caption("Spielerkonfiguration")

    def add_player(self, name, color):
        new_player = Player(name, color)
        self.players.append(new_player)

    def run(self):
        while True:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    pyg.quit()
                    sys.exit()
                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_RETURN:
                        self.save_player_config()
                    elif event.key == pyg.K_TAB:
                        self.switch_player()

                elif event.type == pyg.MOUSEBUTTONDOWN:
                    if self.is_mouse_over_save_button(event.pos):
                        self.save_player_config()
                    elif self.is_mouse_over_color_picker(event.pos):
                        self.show_color_picker()
                        ## Wie machen wir das?

            # Spielfeld aktualisieren
            self.update()

            # Hintergrund zeichnen
            self.screen.fill(self.bg_color)

            # Spielerkonfigurationsformular zeichnen
            self.draw_configuration_form()

            # Fenster aktualisieren
            pyg.display.flip()

    def update(self):
        # Hier könntest du die Spiellogik für die UI-Aktualisierung implementieren
        pass

    def draw_configuration_form(self):
        # Zeichne das Eingabeformular für Spielerkonfiguration
        text = self.font.render(f"Player {self.selected_player} Konfiguration", True, (0, 0, 0))
        self.screen.blit(text, (50, 50))

        name_input_rect = pyg.Rect(50, 100, 200, 32)
        pyg.draw.rect(self.screen, self.input_box_color, name_input_rect)
        name_text = self.font.render(self.player_name_input, True, (0, 0, 0))
        self.screen.blit(name_text, (name_input_rect.x + 5, name_input_rect.y + 5))

        color_picker_rect = pyg.Rect(50, 150, 50, 50)
        pyg.draw.rect(self.screen, self.player_color_input, color_picker_rect)

        save_button_rect = pyg.Rect(50, 220, 100, 40)
        pyg.draw.rect(self.screen, (0, 255, 0), save_button_rect)
        save_text = self.font.render("Speichern", True, (0, 0, 0))
        self.screen.blit(save_text, (save_button_rect.x + 10, save_button_rect.y + 10))

    def save_player_config(self):
        if self.player_name_input:
            player_color = tuple(int(c) for c in self.player_color_input)
            self.add_player(self.player_name_input, player_color)

            if self.selected_player < self.max_players:
                self.selected_player += 1
                self.reset_inputs()
            else:
                print("Alle Spieler konfiguriert!")
                # Hier könntest du die Spielerkonfiguration speichern oder das Spiel starten.

                # Spieler an die PlayerUI übergeben und die PlayerUI starten
                self.player_ui.run()

    def reset_inputs(self):
        self.player_name_input = ""
        self.player_color_input = (255, 0, 0)

    def switch_player(self):
        if self.selected_player < self.max_players:
            self.selected_player += 1
            self.reset_inputs()

    def is_mouse_over_save_button(self, mouse_pos):
        save_button_rect = pyg.Rect(50, 220, 100, 40)
        return save_button_rect.collidepoint(mouse_pos)

    def is_mouse_over_color_picker(self, mouse_pos):
        color_picker_rect = pyg.Rect(50, 150, 50, 50)
        return color_picker_rect.collidepoint(mouse_pos)