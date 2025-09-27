# Combat script
import  pygame as pg
import time
import sys

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis")

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    pg.display.flip()
    clock.tick(60)