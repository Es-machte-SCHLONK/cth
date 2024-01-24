from math import floor

import pygame as pyg


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
                number = font.render(str(counter), True, (230, 0, 0))
                # outline red
                pyg.draw.circle(self.surface, (105, 0, 0), tracker.center, 10, 2)
            else:
                number = font.render(str(counter), True, (220, 220, 220))
                # outline red
                pyg.draw.circle(self.surface, (150, 150, 150), tracker.center, 10, 2)
            self.surface.blit(number_shadow, number.get_rect(
                center=(tracker.center[0] - floor(col_width * 0.75)+2, tracker.center[1]+2)))
            self.surface.blit(number, number.get_rect(
                    center=(tracker.center[0] - floor(col_width * 0.75), tracker.center[1])))
