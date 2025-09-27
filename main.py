# Main script
import  pygame as pg
import time
import sys

# Define Screen size
pg.init()
screen = pg.display.set_mode((1260, 940))
clock = pg.time.Clock()
running = True

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    screen.fill("black")
    pg.display.flip()
    clock.tick(60)