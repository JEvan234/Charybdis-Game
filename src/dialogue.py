# Dialogue Funtions:
import pygame as pg
import time

#global definitions
font = pg.font.Font("Ariel", 24)
class popup:
    def __init__(self,screen, text, font, text_col, x, y):
        self.img = font.render(text, True, text_col)
        self.x = x
        self.y = y
        self.screen = screen

    def draw_text(self):
        self.screen.blit(self.img, (self.x,self.y))