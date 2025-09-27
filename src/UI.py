# Ui frameworks:

import pygame as pg

#Button class:

class Button:
    def __init__(self, x, y, width, height, action=None):
        self.rect = pg.Rect(x, y, width, height)
        self.action = action

    def handle_event(self, event):
        if event.type == pg.MOUSEBUTTONDOWN and event.button == 1: # Left mouse button
            if self.rect.collidepoint(event.pos):
                if self.action:
                    self.action()