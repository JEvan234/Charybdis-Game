# Combat script
import  pygame as pg
import time

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis")
dt = 0

player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)

# Load assets
OceanPath = "./assets/ocean-bg-PLACEHOLDER-1280x960.png"
OceanGraphic = pg.image.load(OceanPath).convert_alpha()
#OceanGraphic = pg.transform.scale(OceanGraphic, (500,500))

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    #screen.fill("blue")
    screen.blit(OceanGraphic, (0,0))

    pg.draw.circle(screen, "red", player_pos, 40)

    keys = pg.key.get_pressed()
    if keys[pg.K_w]:
        player_pos.y -= 300 * dt
    if keys[pg.K_s]:
        player_pos.y += 300 * dt
    if keys[pg.K_a]:
        player_pos.x -= 300 * dt
    if keys[pg.K_d]:
        player_pos.x += 300 * dt

    # flip() the display to put your work on screen
    pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()