import random

import pygame as pyg
from lib.map_surface import map_surface as mas
from lib.players_surface import players_surface as pls
from lib.actions_surface import actions_surface as acs
from lib.conig_surface import config_surface as cfg


class Game:
    def __init__(self):
        pyg.init()
        pyg.display.set_caption('CTH - Catch The Hacker')
        icon = pyg.image.load('lib/icon.png')
        pyg.display.set_icon(icon)
        self.root_width = 1024
        self.root_height = 768
        self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)

        self.running = True
        self.config = cfg.PlayerConfigUI(self.root)
        self.map = mas.Map(self.root)
        self.players = pls.PlayerUI(self.root)
        self.actions = acs.Actions(self.root)
        self.init_players()
        self.selected_position = None  # set on left click

    def handle_events(self):
        if self.config.config_running:
            print("config")
            # Settings window
        else:
            for event in pyg.event.get():
                if event.type == pyg.QUIT:
                    self.running = False
                elif event.type == pyg.KEYDOWN:
                    if event.key == pyg.K_ESCAPE:
                        self.running = False
                elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:  # left click to select node
                    click_pos = event.pos
                    if (click_pos[0] <= self.map.surface.get_width()) and (click_pos[1] <=
                                                                               self.map.surface.get_height()):
                        selected_position = min(self.map.node_positions.keys(),key=lambda pos_xy: self.map.get_distance(pos_xy, click_pos))
                        self.selected_position = selected_position
                        self.map.select_edge(self.selected_position, selected_position)
                    elif (click_pos[0] <= self.players.surface.get_width()) and (click_pos[1] >= self.map.surface.get_height()):
                        print("Click in player surface: " + str(click_pos))
                    elif (click_pos[0] >= self.players.surface.get_width()) and (click_pos[1] >= self.map.surface.get_height()):
                        print("Click in action surface: " + str(click_pos))
                elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 3:  # right click to select player position
                    click_pos = event.pos
                    selected_position = min(self.map.node_positions.keys(), key=lambda pos_xy: self.map.get_distance(
                        pos_xy, click_pos))
                    old_position = (30, 30)
                    self.map.set_player_position(old_position, selected_position, (255, 61, 242))
                elif event.type == pyg.VIDEORESIZE:
                    self.root_width, self.root_height = event.size
                    self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
                    self.config = cfg.PlayerConfigUI(self.root)
                    self.map.__init__(self.root)
                    self.players.__init__(self.root)
                    self.actions.__init__(self.root)

    def render(self):
        if not self.config.config_running:
            self.root.blit(self.map.surface, (0, 0))
            self.root.blit(
                self.players.surface, (0, self.map.surface.get_height())
            )
            self.root.blit(
                self.actions.surface,
                (self.players.surface.get_width(), self.map.surface.get_height())
            )
        else:
            self.root.blit(
                self.config.surface,
                (0, 0)
            )

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            pyg.display.update()

    def set_random_position(self):
        existing_positions = []
        for player in self.players.players:
            existing_positions.append(player.current_position)
        for player in self.players.players:
            position_valid = False
            while not position_valid:
                temp_position = random.choice(list(self.map.node_positions.values()))
                if temp_position not in existing_positions:
                    player.current_position = temp_position
                    position_valid = True

    def init_players(self):
        self.players.add_player("Hunter1", (218, 66, 245))
        print("Player 1 initialisiert.")
        self.players.add_player("Hunter2", (66, 245, 194))
        print("Player 2 initialisiert.")
        self.players.add_player("Hunter3", (245, 138, 66))
        print("Player 3 initialisiert.")
        self.players.add_player("Hunter4", (217, 247, 119))
        print("Player 4 initialisiert.")
        self.players.add_player("LadyX", (191, 191, 191), True)
        print("Lady X initialisiert.")
        self.set_random_position()

        self.players.__init__(self.root)


if __name__ == "__main__":
    game = Game()
    game.run()
    pyg.quit()
