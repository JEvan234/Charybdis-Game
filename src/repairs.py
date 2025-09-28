# Repair script
import  pygame as pg
from pygame import mixer
from sys import exit
import math
import transitions

# Define Repair loop for importing into main
def repair_loop(screen,clock, level):
    mixer.music.pause()

    # Load assets
    OceanPath = "./assets/art/ocean-bg-PLACEHOLDER-1280x960.png"
    OceanGraphic = pg.image.load(OceanPath).convert_alpha()
    #OceanGraphic = pg.transform.scale(OceanGraphic, (500,500))
    ShipPath = "./assets/art/ship-PLACEHOLDER-1280horiz.png" # 420 tall
    Ship = pg.image.load(ShipPath).convert_alpha()

    transitions.fadein(screen, OceanGraphic)

    # Define Player Start positions
    playerStartX = 600
    playerStartY = 450

    # Player Model
    PlayerPath = "./assets/art/player-PLACEHOLDER-80x60.png"
    PlayerModel = pg.image.load(PlayerPath).convert_alpha()

    # General player logic
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
        screen.blit(Ship, (0,260))

        if level == 1:
            pass
        elif level == 2:
            pass
        elif level == 3:
            pass
        elif level == 4:
            pass



        screen.blit(player.image, player.rect)
        player.update()
        # flip() the display to put your work on screen
        pg.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    mixer.init()
    repair_loop(screen = pg.display.set_mode((1280, 960)),clock = pg.time.Clock())