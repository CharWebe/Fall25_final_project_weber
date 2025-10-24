from util_params import *
import pygame
from random import choice

class Chip():
    def __init__(self, x = WIDTH//2, y= HEIGHT//2):
        self.cards = [
            'Fall25_final_project_weber/assets/Chips/chipRedWhite_border.png'
            ]
        self.pick_card = choice(self.cards)
        self.image = pygame.image.load(self.pick_card)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)