# Repair script
import  pygame as pg
from sys import exit

# Define Screen size
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis")
dt = 0

# Enemy list 1-3
#maybe store enemys off screen



def repair_loop():
    # General player logic
    class player:
        def __init__(self, x, y):
            self.rect = pg.Rect(x, y, 80, 60)
            self.x = x
            self.y = y
        
        def blit(self):
            screen.blit(PlayerModel, (self.x,self.y))
    # Define initial player position
    player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
    player_pos.y = 800

    # Load assets
    OceanPath = "./assets/art/ocean-bg-PLACEHOLDER-1280x960.png"
    OceanGraphic = pg.image.load(OceanPath).convert_alpha()
    #OceanGraphic = pg.transform.scale(OceanGraphic, (500,500))
    ShipPath = "./assets/art/ship-PLACEHOLDER-320horiz.png"
    Ship = pg.image.load(ShipPath).convert_alpha()

    # Load Player Assets
    PlayerPath = "./assets/art/player-PLACEHOLDER-80x60.png"
    PlayerModel = pg.image.load(PlayerPath).convert_alpha()

    # Main repair loop
    running = True
    while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    running = False

        # fill the screen with a color to wipe away anything from last frame
        screen.blit(OceanGraphic, (0,0))
        screen.blit(Ship, (0,0))

        # Get/update player movement
        keys = pg.key.get_pressed()
        if keys[pg.K_w]:
            player_pos.y -= 300 * dt
        if keys[pg.K_s]:
            player_pos.y += 300 * dt
        if keys[pg.K_a]:
            player_pos.x -= 300 * dt
        if keys[pg.K_d]:
            player_pos.x += 300 * dt

        # Reflect changes in player movement
        Player1 = player(player_pos.x, player_pos.y)
        Player1.blit()

        # flip() the display to put your work on screen
        pg.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000
