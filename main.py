import pygame as pyg

pyg.init()

root_width = 1024
root_height = 768

root = pyg.display.set_mode((root_width, root_height), pyg.RESIZABLE)

map_height = int(root_height * 0.8)
map_color = (34, 34, 34)
map_surface = pyg.Surface((root_width, map_height))
map_surface.fill(map_color)

players_height = root_height - map_height
players_width = int(root_width * 0.5)
players_color = (0, 100, 0)
players_surface = pyg.Surface((players_width, players_height))
players_surface.fill(players_color)

actions_height = players_height
actions_width = root_width - players_width
actions_color = (138, 0, 0)
actions_surface = pyg.Surface((actions_width, actions_height))
actions_surface.fill(actions_color)

running = True
while running:
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            running = False
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                running = False
        elif event.type == pyg.VIDEORESIZE:
            root_width, root_height = event.size
            root = pyg.display.set_mode((root_width, root_height), pyg.RESIZABLE)
            map_height = int(root_height * 0.8)
            players_height = root_height - map_height
            players_width = int(root_width * 0.5)
            actions_height = players_height
            actions_width = root_width - players_width
            map_surface = pyg.Surface((root_width, map_height))
            players_surface = pyg.Surface((players_width, players_height))
            actions_surface = pyg.Surface((actions_width, actions_height))
            map_surface.fill(map_color)
            players_surface.fill(players_color)
            actions_surface.fill(actions_color)

    root.blit(map_surface, (0, 0))
    root.blit(players_surface, (0, map_height))
    root.blit(actions_surface, (players_width,map_height))
    pyg.display.update()

pyg.quit()
