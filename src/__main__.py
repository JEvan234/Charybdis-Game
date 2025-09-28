# Main script
## RIP the Dream
# Gotta keep the streak going

import  pygame as pg
from pygame import mixer
import UI
from repairs import repair_loop
from combat import combat_loop
import dialogue
import transitions
from time import sleep

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis - KSU Game Jam 2025")

# Music Loading
mixer.init()
mixer.music.load("./assets/music/Menu.wav")
mixer.music.play(loops=-1)
# Define UNIVERSAL integers
BoatHealth = 20

# Load assets
BackgroundPath = "./assets/art/titlescreen-PLACEHOLDER-1280-960.png"
Background = pg.image.load(BackgroundPath).convert_alpha()

LogoPath = "./assets/art/LCKSULogo.png"
LCKSULogo = pg.image.load(LogoPath).convert_alpha()
LCKSULogo = pg.transform.scale(LCKSULogo, (200,200))

PyGameLogoPath = "./assets/art/pygame-ALT-320vert.png"
PygameLogo = pg.image.load(PyGameLogoPath).convert_alpha()
PygameLogo = pg.transform.scale(PygameLogo, (150,150))

# Load popup graphics
textpopup_path = "assets/art/dialogue-BG-1280x960.png"
textBackground = pg.image.load(textpopup_path).convert_alpha()

# Button assets
PlayPath = "./assets/art/playbutton-PLACEHOLDER-320x120.png"
PlayButton = pg.image.load(PlayPath).convert_alpha()
SettingsPath = "assets/art/settingbutton-PLACEHOLDER-320x120.png"
SettingsButton = pg.image.load(SettingsPath).convert_alpha()

# testaction lol - You misread that
joke = False

while running:
    #Get Mouse Position:
    mousePosition = pg.mouse.get_pos()

    #define buttons logically:
    PlayButtonBox = UI.Button(480,420,320,120,True)
    SettingsButtonBox = UI.Button(480,620, 320, 120, True)
    SettingsMeme = dialogue.TextPopup("If you change all the settings, is it still the same game?", (650,660), 1000)

    # Check Quit Condition
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if PlayButtonBox.check_click() == True:
            transitions.fadeout(screen)
            screen.blit(textBackground, (0,0))
            # Intro script goes here
            script = True
            message1 = dialogue.TextPopup("You play as a ship captain eternally bound to the Ship of Theseus as long.", (650,350), 1000)
            message2 = dialogue.TextPopup("In Greek mythology, there is a popular paradox about whether the ship,", (650,400), 1000)
            message3 = dialogue.TextPopup("after full replacement, is still the same ship. Your curse only binds", (650,450), 1000)
            message4 = dialogue.TextPopup("you to the current ship, if you can convince the Sea God that it is a new ", (650,500), 1000)
            message5 = dialogue.TextPopup("ship, and survive the trials of the sea, then you will be released.", (650,550), 1000)
            if script == True:
                message1.draw(screen)
                message2.draw(screen)
                message3.draw(screen)
                message4.draw(screen)
                message5.draw(screen)
            pg.display.flip()
            sleep(15)
            script = False
            combat_loop(screen,clock, 1)
            transitions.fadeout(screen)
            repair_loop(screen,clock,1)
            transitions.fadeout(screen)
            combat_loop(screen,clock, 2)
            transitions.fadeout(screen)
            repair_loop(screen, clock, 2)
            transitions.fadeout(screen)
            combat_loop(screen,clock, 3)
            transitions.fadeout(screen)
            repair_loop(screen, clock, 3)
            transitions.fadeout(screen)
            combat_loop(screen,clock, 4)
            transitions.fadeout(screen)
            screen.blit(textBackground)
            # Intro script goes here
            script = True
            message1 = dialogue.TextPopup("After all the trials of the sea, you were unable to ", (650,350), 1000)
            message2 = dialogue.TextPopup("complete your journey. The monster Charybdis has swallowed the", (650,400), 1000)
            message3 = dialogue.TextPopup("ship whole, leaving nothing to remain. However, this has also freed", (650,450), 1000)
            message4 = dialogue.TextPopup("you of your curse, as the only way to sail again is with a new vessel.", (650,500), 1000)
            if script == True:
                message1.draw(screen)
                message2.draw(screen)
                message3.draw(screen)
                message4.draw(screen)
            pg.display.flip()
            sleep(15)
            screen.fill("black")
            screen.blit(textBackground)
            # Credits
            message1 = dialogue.TextPopup("Programming: Mert Acar, Jacob Evans, Cliff Russell", (650,350), 1000)
            message2 = dialogue.TextPopup("Script: Raam Patel", (650,400), 1000)
            message3 = dialogue.TextPopup("Art: Stephen Colletta, Raam Patel", (650,450), 1000)
            message4 = dialogue.TextPopup("Music: Jeremy Hopkins", (650,500), 1000)
            message5 = dialogue.TextPopup("Special Thanks to LCKSU", (650,550), 1000)
            if script == True:
                message1.draw(screen)
                message2.draw(screen)
                message3.draw(screen)
                message4.draw(screen)
                message5.draw(screen)
            pg.display.flip()
            sleep(15)
            mixer.music.load("./assets/music/Menu.wav")
            mixer.music.play(loops=-1)
        elif SettingsButtonBox.check_click() == True:
            joke = True
            #Debug
            #combat_loop(screen,clock)

    # Load Assets
    screen.blit(Background, (0,0))
    screen.blit(LCKSULogo, (20,750))
    screen.blit(PygameLogo, (240,760))
    if joke == True:
        SettingsMeme.draw(screen)

    

    #Load Button assets
    screen.blit(PlayButton, (480,420)) #(480, 420)
    if joke == False:
        screen.blit(SettingsButton, (480,620)) #480, 620)
    

    pg.display.flip()
    clock.tick(60)
