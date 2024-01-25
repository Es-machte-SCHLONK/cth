import pygame as pyg
import pygame_menu as pm

from lib.players_surface.players_surface import PlayerUI
from main import Game

RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
CYAN = (0, 100, 100)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)


class PlayerConfigUI:
    def __init__(self, root_screen):
        self.created_player = 0
        self.max_players = 4
        self.config_running = True

        # Fenstergröße und Farben
        self.surface = self.init_surface(root_screen)
        self.bg_color = (255, 255, 255)
        self.input_box_color = (200, 200, 200)
        self.font = pyg.font.Font(None, 32)
        self.draw_menu()

    def init_surface(self, root_screen):
        surface = pyg.Surface((root_screen.get_width(), root_screen.get_height()))
        surface.fill(WHITE)
        return surface

    def draw_menu(self):
        colors = [("Red", RED),
                  ("Blue", BLUE),
                  ("Cyan", CYAN),
                  ("Green", GREEN)]

        mainMenu = pm.Menu(title="Main Menu",
                           width=800,
                           height=600,
                           theme=pm.themes.THEME_GREEN)

        mainMenu.add.text_input(title="User Name : ", textinput_id="username")

        mainMenu.add.text_input(title="")

        mainMenu.add.button(title="Create", action=self.createPlayer(mainMenu),
                            font_color=WHITE, background_color=RED)

        mainMenu.draw(self.surface)
        """
        # Exit Button. If clicked, it closes the window
        settings = pm.Menu(title="Settings",
                           width=800,
                           height=500,
                           theme=pm.themes.THEME_GREEN)
        

        mainMenu.add.button(title="Exit", action=self.leave_config(),
                            font_color=WHITE, background_color=RED)

        mainMenu.add.button(title="Create", action=self.createPlayer(settings),
                            font_color=WHITE, background_color=RED)

        # Adjusting the default values
        settings._theme.widget_font_size = 25
        settings._theme.widget_font_color = BLACK
        settings._theme.widget_alignment = pm.locals.ALIGN_LEFT

        # Text input that takes in the username
        settings.add.text_input(title="User Name : ", textinput_id="username")

        # Drop-downs to select the color
        settings.add.dropselect(title="Select Color", items=colors,
                                dropselect_id="color", default=0)
        mainMenu.draw(self.surface)
"""

    def createPlayer(self, settings):
        # getting the data using "get_input_data" method of the Menu class
        settingsData = settings.get_input_data()

        username = settingsData["username"]
        #color = settingsData["color"]
        #PlayerUI.add_player(name=username)
        #PlayerUI.add_player(name=username, color=color)
        self.created_player = self.created_player + 1
        if self.created_player == self.max_players:
            self.leave_config()

    def leave_config(self):
        self.config_running = False
