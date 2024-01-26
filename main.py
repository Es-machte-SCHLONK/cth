import random
from math import floor

import pygame as pyg
from lib.map_surface import map_surface as mas
from lib.players_surface import players_surface as pls
from lib.actions_surface import actions_surface as acs
from lib.config_surface import config_surface as cfg
from lib.x_controls.xcontroller import estimate_move


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
        self.init_players()
        self.selected_position = None# set on left click
        self.action_needed = None

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
                        selected_position = min(self.map.node_positions.keys(),
                                                key=lambda pos_xy: self.map.get_distance(pos_xy, click_pos))
                        # get player on turn
                        active_player = None
                        for player in self.players.players:
                            if player.on_turn:
                                active_player = player

                        destination_node = self.map.select_edge(active_player.current_position, selected_position)
                        if destination_node:
                            # SRC == Y || DST == Y --> Y
                            #   [SRC == G && DST != Y --> G
                            #   DST == G && SRC != Y --> G]
                            #   ELIF SRC == G || DST == G --> G
                            #   [SRC == R && DST == R --> R]
                            #   ELSE R
                            current_node = self.map.node_positions[active_player.current_position]
                            if current_node.yellow or destination_node.yellow:
                                if active_player.yellow > 0:
                                    self.action_needed = "y"
                                    self.selected_position = selected_position
                                    self.actions.draw_turn_button(True)

                            elif current_node.green or destination_node.green:
                                if active_player.green > 0:
                                    self.action_needed = "g"
                                    self.selected_position = selected_position
                                    self.actions.draw_turn_button(True)

                            else:
                                if active_player.red > 0:
                                    self.action_needed = "r"
                                    self.selected_position = selected_position
                                    self.actions.draw_turn_button(True)
                        else:
                            self.selected_position = None
                            # end turn

                    elif (click_pos[0] <= self.players.surface.get_width()) and (
                            click_pos[1] >= self.map.surface.get_height()):
                        print("Click in player surface: " + str(click_pos))
                    elif (click_pos[0] >= self.players.surface.get_width()) and (
                            click_pos[1] >= self.map.surface.get_height()):
                        col_width = floor(self.actions.surface.get_width() / 2 / 7)
                        row_height = floor(self.actions.surface.get_height() / 2 / 7)
                        button_width = col_width * 2.5
                        button_height = row_height * 4
                        end_turn_start_position_x = col_width * 11 + self.players.surface.get_width()
                        end_turn_start_position_y = row_height * 7 + self.map.surface.get_height()
                        end_turn_end_position_x = end_turn_start_position_x + button_width
                        end_turn_end_position_y = end_turn_start_position_y + button_height
                        if (end_turn_start_position_x <= click_pos[0] <= end_turn_end_position_x) and (
                                end_turn_start_position_y <= click_pos[1] <= end_turn_end_position_y):
                            if self.selected_position:
                                self.changePlayer()
                                print("end turn clicked")
                            """
                                active_player_index = None
                                counter = -1
                                active_player = None
                                current_position = None
                                for player in self.players.players:
                                    counter += 1
                                    if player.on_turn:
                                        active_player = player
                                        current_position = player.current_position
                                        active_player_index = counter

                                if active_player_index == (len(self.players.players) - 1):
                                    print("LadyX?")
                                    print("Players Turn: " + self.players.players[0].name)
                                    self.players.players[0].on_turn = True
                                    self.players.players[active_player_index].on_turn = False
                                else:
                                    print("Players Turn: " + self.players.players[active_player_index + 1].name)
                                    self.players.players[active_player_index + 1].on_turn = True
                                    self.players.players[active_player_index].on_turn = False
                            else:
                                print("Button-Not-Active")#Skip player
                            """
                            self.actions.draw_turn_button(False)
                            self.players.init_surface()


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
            for existing_player in self.players.players:
                existing_positions.append(existing_player.current_position)
            position_valid = False
            while not position_valid:
                temp_position = random.choice(list(self.map.node_positions.keys()))
                if temp_position not in existing_positions:
                    player.current_position = temp_position
                    position_valid = True
                existing_positions.clear()

    def init_players(self):
        self.players.add_player("Hunter1", (218, 66, 245))
        self.players.add_player("Hunter2", (66, 245, 194))
        self.players.add_player("Hunter3", (245, 138, 66))
        self.players.add_player("Hunter4", (217, 247, 119))
        self.players.add_player("LadyX", (191, 191, 191), True)
        self.set_random_position()
        for player in self.players.players:
            if not player.ladyX:
                self.map.set_player_position(player.current_position, player.current_position, player.color)
        print(
            "Player 1 initialisiert. " + str(self.map.node_positions[self.players.players[0].current_position].number))
        print(
            "Player 2 initialisiert. " + str(self.map.node_positions[self.players.players[1].current_position].number))
        print(
            "Player 3 initialisiert. " + str(self.map.node_positions[self.players.players[2].current_position].number))
        print(
            "Player 4 initialisiert. " + str(self.map.node_positions[self.players.players[3].current_position].number))
        print("Lady X initialisiert. " + str(self.map.node_positions[self.players.players[4].current_position].number))
        self.players.init_surface()

    def changePlayer(self):
        active_player = None
        player_positions = []
        for player in self.players.players:
            player_positions.append(player.current_position)
            if player.on_turn:
                active_player = player
        index = self.players.players.index(active_player)
        if index == 3:
            print(self.players.players[4].current_position)
            neighbours = self.map.node_positions[self.players.players[4].current_position].neighbours
            new_x_position = estimate_move(player_positions, neighbours)
            print(new_x_position)
            self.players.players[4].current_position = new_x_position

            new_index = 0
        else:
            new_index = index + 1
        self.map.set_player_position(self.players.players[index].current_position, self.selected_position,
                                     self.players.players[index].color)
        self.players.players[index].current_position = self.selected_position
        if self.action_needed == "y":
            self.players.players[index].yellow = self.players.players[index].yellow - 1
        elif self.action_needed == "g":
            self.players.players[index].green = self.players.players[index].green - 1
        elif self.action_needed == "r":
            self.players.players[index].red = self.players.players[index].red - 1
        else:
            print("Fehler: Kein Ticket verwendet!")
        self.players.players[index].on_turn = False
        self.players.players[new_index].on_turn = True
        self.map.draw_edges()
        self.map.draw_nodes()
        self.players.init_surface()

if __name__ == "__main__":
    game = Game()
    game.run()
    pyg.quit()
# ha