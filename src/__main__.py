# Main script
import  pygame as pg
import UI
import time

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis - KSU Game Jam 2025")


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

# Define Buttons Logically
def testaction():
    print("yep")

while running:
    #Get Mouse Position:
    mousePosition = pg.mouse.get_pos()

    #define buttons logically:
    PlayButtonBox = UI.Button(480,420,320,120,True)

    # Check Quit Condition
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False
        elif event.type == pg.KEYDOWN:
            if event.key == pg.K_ESCAPE:
                running = False
        if PlayButtonBox.check_click() == True:
            print("yep")
            time.sleep(0.1)
        # Check mouse clicks


    # Load Assets
    screen.blit(Background, (0,0))
    screen.blit(LCKSULogo, (20,750))
    screen.blit(PygameLogo, (240,760))

    #Load Button assets
    screen.blit(PlayButton, (480,420)) #(480, 420)
    screen.blit(SettingsButton, (480,620)) #480, 220)
    # Load play button hit-boxes
    

    pg.display.flip()
    clock.tick(60)