# Main script
## RIP the Dream

import  pygame as pg
from pygame import mixer
import UI
from repairs import repair_loop
from combat import combat_loop
import dialogue
import transitions

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
            combat_loop(screen,clock, 1)
            transitions.fadeout(screen)
            #transitions.fadeout(screen)
            combat_loop(screen,clock, 2)
            transitions.fadeout(screen)
            #repair_loop(screen, clock, 2)
            #transitions.fadeout(screen)
            combat_loop(screen,clock, 3)
            transitions.fadeout(screen)
            #repair_loop(screen, clock, 3)
            #transitions.fadeout(screen)
            combat_loop(screen,clock, 4)
            #transitions.fadeout(screen)
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