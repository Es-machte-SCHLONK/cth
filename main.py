import pygame as pyg
from cth.lib import graph
from cth.lib import guisurfaces as gui


class Game:
    def __init__(self):
        pyg.init()
        self.root_width = 1024
        self.root_height = 768
        self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
        self.running = True
        self.gui_surfaces = gui.GuiSurfaces(self.root)

    def handle_events(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.running = False
                if event.key == pyg.K_SPACE:
                    print("Male Karte")
                    self.gui_surfaces.draw_map_surface(10)
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
