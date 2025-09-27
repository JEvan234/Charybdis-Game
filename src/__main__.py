# Main script
import  pygame as pg
import time

# Define Screen size
pg.init()
screen = pg.display.set_mode((1280, 960))
clock = pg.time.Clock()
running = True
pg.display.set_caption("Charybdis - KSU Game Jam 2025")


# Load assets
BackgroundPath = "./assets/titlescreen-PLACEHOLDER-1280-960.png"
Background = pg.image.load(BackgroundPath).convert_alpha()

LogoPath = "./assets/LCKSULogo.png"
LCKSULogo = pg.image.load(LogoPath).convert_alpha()
LCKSULogo = pg.transform.scale(LCKSULogo, (200,200))

PyGameLogoPath = "./assets/pygame_logo.png"
PygameLogo = pg.image.load(PyGameLogoPath).convert_alpha()
PygameLogo = pg.transform.scale(PygameLogo, (200,100))


while running:
    #Get Mouse Position:
    mouse_x, mouse_y = pg.mouse.get_pos()

    # Check Quit Condition
    for event in pg.event.get():
        if event.type == pg.QUIT:
            running = False

    # Load Assets
    screen.blit(Background, (0,0))
    screen.blit(LCKSULogo, (20,720))
    screen.blit(PygameLogo, (240,800))

    #Load Button assets
    #(480, 420)
    #480, 220)

    # Check Mouse over buttons
    


    pg.display.flip()
    clock.tick(60)