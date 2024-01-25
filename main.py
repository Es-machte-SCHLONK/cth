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
        self.root = pyg.display.set_mode((self.root_width, self.root_height))

        self.running = True
        self.config = cfg.PlayerConfigUI(self.root)
        self.map = mas.Map(self.root)
        self.players = pls.PlayerUI(self.root)
        self.actions = acs.Actions(self.root)
        self.selected_position = None  # set on left click

    def handle_events(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.running = False
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 1:  # left click to select node
                if not self.config.config_running:
                    click_pos = event.pos
                    if (click_pos[0] <= self.map.surface.get_width()) and (
                            click_pos[1] <= self.map.surface.get_height()):
                        selected_position = min(self.map.node_positions.keys(),
                                                key=lambda pos_xy: self.map.get_distance(
                                                    pos_xy, click_pos))
                        self.map.select_node(selected_position)
                        self.selected_position = selected_position
                    elif (click_pos[0] <= self.players.surface.get_width()) and (
                            click_pos[1] >= self.map.surface.get_height()):
                        print("Click in player surface: " + str(click_pos))
                    elif (click_pos[0] >= self.players.surface.get_width()) and (
                            click_pos[1] >= self.map.surface.get_height()):
                        print("Click in action surface: " + str(click_pos))
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 4:  # scroll up to test edge selection
                click_pos = event.pos
                selected_position = min(self.map.node_positions.keys(), key=lambda pos_xy: self.map.get_distance(
                    pos_xy, click_pos))
                if self.selected_position is not None:
                    self.map.select_edge(self.selected_position, selected_position)
                else:
                    print("First select start node with left click")
            elif event.type == pyg.MOUSEBUTTONDOWN and event.button == 3:  # right click to select player position
                click_pos = event.pos
                selected_position = min(self.map.node_positions.keys(), key=lambda pos_xy: self.map.get_distance(
                    pos_xy, click_pos))
                old_position = (30, 30)
                self.map.set_player_position(old_position, selected_position, (255, 61, 242))

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
                (self.config.surface.get_width(), self.map.surface.get_height())
            )

    def run(self):
        while self.running:
            self.handle_events()
            self.render()
            pyg.display.update()


if __name__ == "__main__":
    game = Game()
    game.run()
    pyg.quit()
