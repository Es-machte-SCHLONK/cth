from math import floor

import pygame as pyg
import lib.players_surface.Player as player


class LadyX_tracker:
    def __init__(self):
        self.color = (255, 255, 255)
        self.node_number = None
        self.show = False
        self.set = False
        self.node_position = None
        self.node = None
        self.center = None


class Actions:
    def __init__(self, root_screen):
        self.color = (34, 34, 34)
        self.surface = None
        self.root_height = root_screen.get_height()
        self.root_width = root_screen.get_width()
        self.x_trackers = []
        self.init_surface()
        self.generate_x_counters()
        self.draw_x_counters()
        self.draw_turn_button()

    def init_surface(self):
        self.surface = pyg.Surface(
            (
                (self.root_width - int(self.root_width * 0.5)), (self.root_height - int(self.root_height * 0.8))
            )
        )
        self.surface.fill(self.color)

    def generate_x_counters(self):
        for i in range(0, 24):
            tracker = LadyX_tracker()
            if (i == 2) or (i == 7) or (i == 12) or (i == 17) or (i == 23):
                tracker.show = True
            self.x_trackers.append(tracker)

    def draw_x_counters(self):
        """
        Layout Actions
        |   Headline            |    Headline            |
        |  | 1 | 7 | 13 | 19 |  | <Playername>           |
        |  | 2 | X | X  | X  |  |                        |
        |  | 3 | X | X  | X  |  |       Tickets left     |
        |  | 4 | X | X  | X  |  |   |  | Y | G | R |  |  |
        |  | X | X | X  | X  |  |                        |
        |  | X | X | X  | X  |  |                        |
        2 x 50%
        each side 7 rows, 7 cols
        """
        col_width = floor(self.surface.get_width() / 2 / 7)
        row_height = floor(self.surface.get_height() / 2 / 7)

        font = pyg.font.SysFont("arial bold", 20)
        row_counter = 0
        col_counter = 1
        counter = 0
        for tracker in self.x_trackers:
            counter += 1
            row_counter += 1
            if row_counter > 6:
                row_counter = 1
                col_counter += 1
            tracker.center = (floor(col_width * 1.5 * col_counter),
                              floor(row_height * 2 * row_counter))

            # shadow
            pyg.draw.circle(self.surface, (10, 10, 10), (tracker.center[0] + 2, tracker.center[1] + 2), 10)
            # background
            pyg.draw.circle(self.surface, tracker.color, tracker.center, 10)
            # inner shadow outline
            pyg.draw.circle(self.surface, (15, 15, 15), tracker.center, 10, 3)
            number_shadow = font.render(str(counter), True, (10, 10, 10))
            if tracker.show:

                if tracker.node:
                    node_font = pyg.font.SysFont("arial bold", 15)
                    x_counter_no = node_font.render(str(tracker.node.number), True, (0, 0, 0))
                    self.surface.blit(x_counter_no, x_counter_no.get_rect(center=tracker.center))
                number = font.render(str(counter), True, (230, 0, 0))
                # outline red
                pyg.draw.circle(self.surface, (105, 0, 0), tracker.center, 10, 2)

            else:
                number = font.render(str(counter), True, (220, 220, 220))
                # outline normal
                pyg.draw.circle(self.surface, (150, 150, 150), tracker.center, 10, 2)
            self.surface.blit(number_shadow, number.get_rect(
                center=(tracker.center[0] - floor(col_width * 0.75) + 2, tracker.center[1] + 2)))
            self.surface.blit(number, number.get_rect(
                center=(tracker.center[0] - floor(col_width * 0.75), tracker.center[1])))

    def draw_player_state(self, player):
        col_width = floor(self.surface.get_width() / 2 / 7)
        row_height = floor(self.surface.get_height() / 2 / 7)
        font = pyg.font.SysFont("arial bold", 24)
        player_name_text = font.render(player.name, True, (220, 220, 220))
        pyg.draw.rect(self.surface, (34, 34, 34),
                      (floor(col_width * 6.5), row_height, floor(col_width * 7.5), row_height * 5))
        self.surface.blit(player_name_text, player_name_text.get_rect(
            center=(floor(col_width * 7.5), row_height * 2)))
        font = pyg.font.SysFont("arial bold", 20)
        tickets_headline = font.render("Actions:", True, (220, 220, 220))
        self.surface.blit(tickets_headline, player_name_text.get_rect(
            center=(floor(col_width * 7.5), row_height * 5)))

        font = pyg.font.SysFont("arial bold", 20)

        # yellow
        yellow = font.render(str(player.yellow), True, (0, 0, 0))
        pyg.draw.circle(self.surface, (10, 10, 10), (col_width * 7.2 + 3, row_height * 9 + 3), 20)
        pyg.draw.circle(self.surface, (255, 250, 97), (col_width * 7.2, row_height * 9), 20)
        pyg.draw.circle(self.surface, (15, 15, 15), (col_width * 7.2, row_height * 9), 20, 3)
        pyg.draw.circle(self.surface, (150, 150, 150), (col_width * 7.2, row_height * 9), 20, 2)
        self.surface.blit(yellow, yellow.get_rect(
            center=(col_width * 7.2, row_height * 9)))
        # green
        green = font.render(str(player.green), True, (0, 0, 0))
        pyg.draw.circle(self.surface, (10, 10, 10), (col_width * 8.5 + 3, row_height * 9 + 3), 20)
        pyg.draw.circle(self.surface, (66, 219, 73), (col_width * 8.5, row_height * 9), 20)
        pyg.draw.circle(self.surface, (15, 15, 15), (col_width * 8.5, row_height * 9), 20, 3)
        pyg.draw.circle(self.surface, (150, 150, 150), (col_width * 8.5, row_height * 9), 20, 2)
        self.surface.blit(green, yellow.get_rect(
            center=(col_width * 8.55, row_height * 9)))
        # red
        red = font.render(str(player.red), True, (0, 0, 0))
        pyg.draw.circle(self.surface, (10, 10, 10), (col_width * 9.75 + 3, row_height * 9 + 3), 20)
        pyg.draw.circle(self.surface, (255, 107, 97), (col_width * 9.75, row_height * 9), 20)
        pyg.draw.circle(self.surface, (15, 15, 15), (col_width * 9.75, row_height * 9), 20, 3)
        pyg.draw.circle(self.surface, (150, 150, 150), (col_width * 9.75, row_height * 9), 20, 2)
        self.surface.blit(red, yellow.get_rect(
            center=(col_width * 9.8, row_height * 9)))

    def draw_turn_button(self, active=False):
        col_width = floor(self.surface.get_width() / 2 / 7)
        row_height = floor(self.surface.get_height() / 2 / 7)
        button_active = False
        button_width = col_width * 2.5
        button_height = row_height * 4
        if active:
            button_color = (6, 48, 18)
        else:
            button_color = (48, 6, 6)

        button_text = "End Turn"
        button_font = pyg.font.SysFont("arial bold", 20)
        button_text_render = button_font.render(button_text, True, (255, 255, 255))
        button_rect = pyg.Rect(
            col_width * 11,
            row_height * 7,
            button_width,
            button_height
        )
        button_shadow_rect = pyg.Rect(
            col_width * 11 + 30,
            row_height * 7 + 3,
            button_width,
            button_height
        )
        pyg.draw.rect(self.surface, (10, 10, 10),
                      (col_width * 11 + 3, row_height * 7 + 3, button_width, button_height),
                      0, 10)
        pyg.draw.rect(self.surface, button_color,
                      (col_width * 11, row_height * 7, button_width, button_height),
                      0, 10)
        self.surface.blit(button_text_render, button_text_render.get_rect(center=button_rect.center))
