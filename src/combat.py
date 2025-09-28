# Combat script
import  pygame as pg
from pygame import mixer
from sys import exit
import time
import math

#player_pos = pg.Vector2(screen.get_width() / 2, screen.get_height() / 2)
#player_pos.y = 800
def combat_loop(screen,clock):
    mixer.music.pause()
    playerStartX = 300
    playerStartY = 300

    ARROW_SCALE = 1.0
    ARROW_SPEED = 10
    ARROW_LIFETIME = 1750 #this is in milliseconds!!!

    PLAYER_SPEED = 8

    GUN_OFFSET_X = 45
    GUN_OFFSET_Y = 20

    SHOOT_COOLDOWN = 20


    # Enemy list 1-3
    #maybe store enemys off screen

    # Load assets
    OceanPath = "./assets/art/ocean-bg-PLACEHOLDER-1280x960.png"
    OceanGraphic = pg.image.load(OceanPath).convert_alpha()
    ShipPath = "./assets/art/ship-PLACEHOLDER-1280horiz.png"
    Ship = pg.image.load(ShipPath).convert_alpha()

    PlayerPath = "./assets/art/player-PLACEHOLDER-80x60.png"
    PlayerModel = pg.image.load(PlayerPath).convert_alpha()

    ArrowPath = "./assets/art/arrow-PLACEHOLDER-cropped.png"
    ArrowModel = pg.image.load(ArrowPath).convert_alpha()

    class Player(pg.sprite.Sprite):
        def __init__(self):
            super().__init__()
            self.pos =  pg.Vector2(playerStartX, playerStartY)

            self.image = PlayerModel
            self.base_player_image = self.image

            self.hitbox_rect = self.base_player_image.get_rect(center = self.pos)
            self.rect= self.hitbox_rect.copy()

            self.speed = PLAYER_SPEED

            self.shoot = False
            self.shoot_cooldown = 0
            self.angle = 0

            self.gun_barrel_offset = pg.math.Vector2(GUN_OFFSET_X, GUN_OFFSET_Y)

        
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

            if pg.mouse.get_pressed() == (1, 0, 0) or keys[pg.K_SPACE]:
                self.shoot = True
                self.is_shooting()
            else:
                self.shoot = False

        def is_shooting(self): 
            if self.shoot_cooldown == 0:
                self.shoot_cooldown = SHOOT_COOLDOWN
                spawn_arrow_pos = self.pos + self.gun_barrel_offset.rotate(self.angle)
                self.bullet = Arrow(spawn_arrow_pos[0], spawn_arrow_pos[1], self.angle + 270)
                bullet_group.add(self.bullet)
                all_sprites_group.add(self.bullet)

        def move(self):
            self.pos += pg.math.Vector2(self.velocity_x, self.velocity_y)
            self.hitbox_rect.center = self.pos
            self.rect.center = self.hitbox_rect.center

        def update(self):
            self.user_input()
            self.move()
            self.player_rotation()

            if self.shoot_cooldown > 0:
                self.shoot_cooldown -= 1

    # Class to create multiple arrows at a time
    class Arrow(pg.sprite.Sprite):
        def __init__(self, x, y, angle):
            super().__init__()
            self.image = ArrowModel
            self.image = pg.transform.rotozoom(self.image, 0, ARROW_SCALE)
            self.base_arrow_image = self.image

            self.rect = self.image.get_rect()
            self.rect.center = (x, y)
            self.x = x
            self.y = y
            self.angle = angle
            self.speed = ARROW_SPEED
            self.x_vel = math.cos(self.angle * (2*math.pi/360)) * self.speed
            self.y_vel = math.sin(self.angle * (2*math.pi/360)) * self.speed
            self.arrow_lifetime = ARROW_LIFETIME
            self.spawn_time = pg.time.get_ticks() # gets the specific time that the bullet was created

            self.image = pg.transform.rotate(self.base_arrow_image, -(self.angle + 180)) #transformation to properly orient arrows
            

        def arrow_movement(self):  
            self.x += self.x_vel
            self.y += self.y_vel

            self.rect.x = int(self.x)
            self.rect.y = int(self.y)

            if pg.time.get_ticks() - self.spawn_time > self.arrow_lifetime:
                self.kill() 

        def update(self):
            self.arrow_movement()

    player = Player()

    all_sprites_group = pg.sprite.Group()
    bullet_group = pg.sprite.Group()

    all_sprites_group.add(player)

    # Main Combat Loop
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

        screen.blit(OceanGraphic, (0,0))
        screen.blit(Ship, (0,730))
        #screen.blit(player.image, player.rect)

        all_sprites_group.draw(screen)
        all_sprites_group.update()

        #debug imagery
        pg.draw.rect(screen, "red", player.hitbox_rect, width=2)
        pg.draw.rect(screen, "yellow", player.rect, width=2)

        #poorly made debug to see hitboxes of arrow sprites, need to rework (or redesign stuff)
        for sprite in all_sprites_group:
            pg.draw.rect(screen, "blue", sprite.rect, 2)


        pg.display.flip()
        clock.tick(60)

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        # dt = clock.tick(60) / 1000

if __name__ == "__main__":
    screen = pg.display.set_mode((1280, 960))
    clock = pg.time.Clock()
    mixer.init()
    combat_loop(screen, clock)