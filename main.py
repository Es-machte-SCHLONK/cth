import pygame as pyg


class GuiSurfaces:
    def __init__(self, root):
        self.map_surface = None
        self.players_surface = None
        self.actions_surface = None
        self.root_height = root.get_height()
        self.root_width = root.get_width()
        # 1. map, 2. players, 3. actions!
        self.init_map_surfaces()
        self.init_players_surfaces()
        self.init_actions_surfaces()

    def init_map_surfaces(self):
        map_height = int(self.root_height * 0.8)
        map_color = (34, 34, 34)
        self.map_surface = pyg.Surface((self.root_width, map_height))
        self.map_surface.fill(map_color)

    def init_players_surfaces(self):
        players_height = self.root_height - self.map_surface.get_height()
        players_width = int(self.root_width * 0.5)
        players_color = (0, 100, 0)
        self.players_surface = pyg.Surface((players_width, players_height))
        self.players_surface.fill(players_color)

    def init_actions_surfaces(self):
        actions_height = self.players_surface.get_height()
        actions_width = self.root_width - self.players_surface.get_width()
        actions_color = (138, 0, 0)
        self.actions_surface = pyg.Surface((actions_width, actions_height))
        self.actions_surface.fill(actions_color)


class Game:
    def __init__(self):
        pyg.init()
        self.root_width = 1024
        self.root_height = 768
        self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
        self.running = True
        self.gui_surfaces = GuiSurfaces(self.root)

    def handle_events(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.running = False
            elif event.type == pyg.VIDEORESIZE:
                self.root_width, self.root_height = event.size
                self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
                self.gui_surfaces.__init__(self.root)

    def render(self):

        self.root.blit(self.gui_surfaces.map_surface, (0, 0))
        self.root.blit(
            self.gui_surfaces.players_surface, (0, self.gui_surfaces.map_surface.get_height())
        )
        self.root.blit(
            self.gui_surfaces.actions_surface,
            (self.gui_surfaces.players_surface.get_width(), self.gui_surfaces.map_surface.get_height())
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
