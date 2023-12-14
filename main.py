import pygame as pyg
import sys
from lib import nodes as Node

pyg.init()

display_width = 1024
display_height = 768
caption = "Catch the Hacker!"
background = (34, 34, 34)
fps = 30

display = pyg.display.set_mode((display_width, display_height), pyg.RESIZABLE)
clock = pyg.time.Clock()
pyg.display.set_caption(caption)
running = True


while running:
    # Handling Keyboard Input
    for event in pyg.event.get():
        if event.type == pyg.QUIT:
            pyg.quit()
            sys.exit()
        elif event.type == pyg.KEYDOWN:
            if event.key == pyg.K_ESCAPE:
                running = False

    display.fill(background)
    pyg.display.update()
    tick = clock.tick(fps)
