# Dialogue Funtions:
import pygame as pg

# init
pg.init()
pg.font.init()

FontPath = "./assets/fonts/Constantine.ttf"
FontSize = 24
Constantine = pg.font.Font(FontPath, FontSize)


'''
text color = #321902
text color = (50, 25, 2)

'''


class TextPopup:
    def __init__(self, text, position, duration_ms):
        self.text = text
        self.font = Constantine
        self.color = "white"
        self.position = position
        self.duration_ms = duration_ms
        self.start_time = pg.time.get_ticks()
        self.surface = self.font.render(self.text, True, self.color)
        self.rect = self.surface.get_rect(center=self.position)

    def update(self):
        # Check if the popup's duration has expired
        if pg.time.get_ticks() - self.start_time >= self.duration_ms:
            return False  # Indicate that the popup should be removed
        return True  # Indicate that the popup is still active

    def draw(self, screen):
        screen.blit(self.surface, self.rect)