# Combat script
import  pygame as pg
from sys import exit
import time
import math

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis")
#dt = 0

#player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#player_pos.y = 800

playerStartX = 300
playerStartY = 300

# Enemy list 1-3
#maybe store enemys off screen

# Load assets
OceanPath = "./assets/art/ocean-bg-PLACEHOLDER-1280x960.png"
OceanGraphic = pg.image.load(OceanPath).convert_alpha()

PlayerPath = "./assets/art/player-PLACEHOLDER-80x60.png"
PlayerModel = pg.image.load(PlayerPath).convert_alpha()

# Class to create multiple arrows at a time
class Arrows:
    def __init__(self, position):
        self.position = position

class Player(pg.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = PlayerModel
        self.base_player_image = self.image

        self.pos =  pg.Vector2(playerStartX, playerStartY)
        self.speed = 8

        self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
        self.rect= self.hitbox_rect.copy()

        

    def player_rotation(self):
        self.mouse_coords = pg.mouse.get_pos()
        self.x_change_mouse_player = (self.mouse_coords[0] - self.hitbox_rect.centerx)
        self.y_change_mouse_player = (self.mouse_coords[1] - self.hitbox_rect.centery)
        self.angle = 90 + math.degrees(math.atan2(self.y_change_mouse_player, self.x_change_mouse_player))
        self.image = pg.transform.rotate(self.base_player_image, -self.angle)
        self.rect = self.image.get_rect(center = self.hitbox_rect.center)

    def user_input(self):
        self.velocity_x = 0
        self.velocity_y = 0

        keys = pg.key.get_pressed()

        if keys[pg.K_w]:
            self.velocity_y = -self.speed
        if keys[pg.K_a]:
            self.velocity_x = -self.speed
        if keys[pg.K_s]:
            self.velocity_y = self.speed
        if keys[pg.K_d]:
            self.velocity_x = self.speed

        if self.velocity_x != 0 and self.velocity_y != 0:
            self.velocity_x /= math.sqrt(2)
            self.velocity_y /= math.sqrt(2)


    def move(self):
        self.pos += pg.math.Vector2(self.velocity_x, self.velocity_y)
        self.hitbox_rect.center = self.pos
        self.rect.center = self.hitbox_rect.center

    def update(self):
        self.user_input()
        self.move()
        self.player_rotation()

player = Player()

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False

    screen.blit(OceanGraphic, (0,0))
    screen.blit(player.image, player.rect)
    player.update()

    #debug imagery
    pg.draw.rect(screen, "red", player.hitbox_rect, width=2)
    pg.draw.rect(screen, "yellow", player.rect, width=2)


    pg.display.update()
    #pg.display.flip()

    # limits FPS to 60
    # dt is delta time in seconds since last frame, used for framerate-
    # independent physics.
    dt = clock.tick(60) / 1000

pg.quit()