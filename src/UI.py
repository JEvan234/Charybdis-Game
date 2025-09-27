# Ui frameworks:

import pygame as pg

#Button class:

class Button:
    def __init__(self, x, y, width, height, enabled):
        self.rect = pg.Rect(x, y, width, height)
        self.enabled = enabled

    def check_click(self):
        mouse_pos = pg.mouse.get_pos()
        left_click = pg.mouse.get_pressed()[0]
        if left_click and self.rect.collidepoint(mouse_pos) and self.enabled:
            return True
        else:
            return False