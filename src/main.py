# Main script
import  pygame as pg
import time

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis")

# Load assets
LogoPath = "./assets/LCKSULogo.png"
LCKSULogo = pg.image.load(LogoPath).convert_alpha()
LCKSULogo = pg.transform.scale(LCKSULogo, (500,500))

while running:
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
    for i in range (100, 0,-10):
        LCKSULogo.set_alpha(i)
    screen.blit(LCKSULogo, (390,230))
    pg.display.flip()
    clock.tick(60)