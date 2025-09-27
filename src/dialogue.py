# Dialogue Funtions:
import pygame as pg

class TextPopup:
    def __init__(self, text, font, color, position, duration_ms):
        self.text = text
        self.font = font
        self.color = color
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