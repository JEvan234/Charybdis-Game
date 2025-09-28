# Repair script
import  pygame as pg
from pygame import mixer
from sys import exit
import math
import transitions
import UI
from time import sleep
import dialogue

# Define Repair loop for importing into main
def repair_loop(screen,clock, level):
    mixer.music.pause()
    mixer.music.load("./assets/music/ShopLofi.wav")
    mixer.music.play(loops=-1)
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
    PlayerPath = "./assets/art/player-STANDING-110x60.png"
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

            '''if keys[pg.K_w]:
                self.velocity_y = -self.speed
            if keys[pg.K_a]:
                self.velocity_x = -self.speed
            if keys[pg.K_s]:
                self.velocity_y = self.speed
            if keys[pg.K_d]:
                self.velocity_x = self.speed
'''
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

    #Load progress graphics
    ProgressPath1 = "./assets/art/progressbar-1PROGRESS-640x60.png"
    ProgressPath2 = "./assets/art/progressbar-2PROGRESS-640x60.png"
    ProgressPath3 = "./assets/art/progressbar-3PROGRESS-640x60.png"
    ProgressPath4 = "./assets/art/progressbar-4PROGRESS-640x60.png"

    ProgressGraphic2 = pg.image.load(ProgressPath2).convert_alpha()
    ProgressGraphic3 = pg.image.load(ProgressPath3).convert_alpha()
    ProgressGraphic4 = pg.image.load(ProgressPath4).convert_alpha()

    # Load popup graphics
    textpopup_path = "assets/art/dialogue-BG-1280x960.png"
    textBackground = pg.image.load(textpopup_path).convert_alpha()


    # Load Player Assets
    PlayerPath = "./assets/art/player-PLACEHOLDER-80x60.png"
    PlayerModel = pg.image.load(PlayerPath).convert_alpha()

    # Add ship elements:
    Chest_path = "./assets/art/chest2.png"
    Chest = pg.image.load(Chest_path).convert_alpha()
    mat_path = "./assets/art/player-mat-80x60.png"
    mat = pg.image.load(mat_path).convert_alpha()
    wheel_path = "./assets/art/ships-wheel-80x60.png"
    wheel = pg.image.load(wheel_path).convert_alpha()
    
    Boardrepairs = False
    # Main repair loop
    running = True
    while running:
        ChestBox = UI.Button(550,350, 64, 64, True)
        Carry_foward = UI.Button(725,425, 80, 60, True)
        matUI = UI.Button(400,425, 80, 60, True)
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
        for event in pg.event.get():
            if event.type == pg.QUIT:
                exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE:
                    exit()
            if Carry_foward.check_click() == True:
                running = False
            if ChestBox.check_click() == True:
                screen.blit(textBackground, (0,0))
                Boardrepairs = True
                repair_message = dialogue.TextPopup("You Repair and exchange the planks of the ship", (650,350), 1000)
                debate = dialogue.TextPopup("After all the repairs is it still the same ship?", (650,400), 1000)
                if Boardrepairs == True:
                    repair_message.draw(screen)
                    debate.draw(screen)
                pg.display.flip()
                sleep(5)


        # fill the screen with a color to wipe away anything from last frame
        screen.blit(OceanGraphic, (0,0))
        screen.blit(Ship, (0,260))
        screen.blit(wheel, (725, 425))
        screen.blit(Chest, (550,350))
        screen.blit(mat, (400, 425))
        screen.blit(player.image, player.rect)
        player.update()
        

        if level == 1:
            screen.blit(ProgressGraphic2, (0,0))
            if matUI.check_click() == True:
                screen.blit(textBackground, (0,0))
                script = True
                message1 = dialogue.TextPopup("After enduring your first encounter, you plead with the sea god.", (650,350), 1000)
                message2 = dialogue.TextPopup("You beg to be released from the ship, explaining that the ", (650,400), 1000)
                message3 = dialogue.TextPopup("planks are no longer original, and thus the ship is new.", (650,450), 1000)
                message4 = dialogue.TextPopup("The Sea god does not listen, he argues that the ship still floats, ", (650,500), 1000)
                message5 = dialogue.TextPopup("just as it had when you embarked on yor journey.", (650,550), 1000)
                if script == True:
                    message1.draw(screen)
                    message2.draw(screen)
                    message3.draw(screen)
                    message4.draw(screen)
                    message5.draw(screen)
                pg.display.flip()
                sleep(10)
        elif level == 2:
            screen.blit(ProgressGraphic3, (0,0))
            if matUI.check_click() == True:
                screen.blit(textBackground, (0,0))
                script = True
                message1 = dialogue.TextPopup("You once again plea with the god, begging for release.", (650,350), 1000)
                message2 = dialogue.TextPopup("You argue that the ship itsself has seen many new battles,", (650,400), 1000)
                message3 = dialogue.TextPopup("and thus is no longer the same ship.", (650,450), 1000)
                message4 = dialogue.TextPopup("The sea god ignores the captain's crys, and insists", (650,500), 1000)
                message5 = dialogue.TextPopup("that the ship is still the same.", (650,550), 1000)
                if script == True:
                    message1.draw(screen)
                    message2.draw(screen)
                    message3.draw(screen)
                    message4.draw(screen)
                    message5.draw(screen)
                pg.display.flip()
                sleep(10)
        elif level == 3:
            screen.blit(ProgressGraphic4, (0,0))
            if matUI.check_click() == True:
                screen.blit(textBackground, (0,0))
                script = True
                message1 = dialogue.TextPopup("You beg for release one final time, arguing that", (650,350), 1000)
                message2 = dialogue.TextPopup("You are no longer the same, the seas have changed you, and as the", (650,400), 1000)
                message3 = dialogue.TextPopup("captain, this change extends to the ship", (650,450), 1000)
                message4 = dialogue.TextPopup("The sea god reminds you that the ship still stands,", (650,500), 1000)
                message5 = dialogue.TextPopup("and ignores any furthur pleas.", (650,550), 1000)
                if script == True:
                    message1.draw(screen)
                    message2.draw(screen)
                    message3.draw(screen)
                    message4.draw(screen)
                    message5.draw(screen)
                pg.display.flip()
                sleep(10)
        elif level == 4:
            pass


        
        # flip() the display to put your work on screen
        pg.display.flip()

        # limits FPS to 60
        # dt is delta time in seconds since last frame, used for framerate-
        # independent physics.
        dt = clock.tick(60) / 1000

if __name__ == "__main__":
    mixer.init()
    repair_loop(level=3,screen = pg.display.set_mode((1280, 960)),clock = pg.time.Clock())