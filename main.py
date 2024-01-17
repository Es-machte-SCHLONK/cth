import pygame as pyg
from lib.map_surface import map_surface as mas
from lib.players_surface import players_surface as pls
from lib.actions_surface import actions_surface as acs

class Game:
    def __init__(self):
        pyg.init()
        self.root_width = 1024
        self.root_height = 768
        self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
        self.running = True
        self.maps = mas.Maps(self.root)
        self.players = pls.Players(self.root)
        self.actions = acs.Actions(self.root)

    def handle_events(self):
        for event in pyg.event.get():
            if event.type == pyg.QUIT:
                self.running = False
            elif event.type == pyg.KEYDOWN:
                if event.key == pyg.K_ESCAPE:
                    self.running = False
                #if event.key == pyg.K_SPACE:
                    #self.maps.draw_map_surface(10)
            elif event.type == pyg.VIDEORESIZE:
                self.root_width, self.root_height = event.size
                self.root = pyg.display.set_mode((self.root_width, self.root_height), pyg.RESIZABLE)
                self.maps.__init__(self.root)
                self.players.__init__(self.root)
                self.actions.__init__(self.root)

    def render(self):
        self.root.blit(self.maps.surface, (0, 0))
        self.root.blit(
            self.players.surface, (0, self.maps.surface.get_height())
        )
        self.root.blit(
            self.actions.surface,
            (self.players.surface.get_width(), self.maps.surface.get_height())
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
