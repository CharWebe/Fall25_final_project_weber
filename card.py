from util_params import *
import pygame
from random import choice

class Card():
    def __init__(self, x = WIDTH//2, y= HEIGHT//2):
        self.cards = [
            'Fall25_final_project_weber/assets/Cards/cardClubs2.png','Fall25_final_project_weber/assets/Cards/cardClubs3.png',
            'Fall25_final_project_weber/assets/Cards/cardClubs4.png','Fall25_final_project_weber/assets/Cards/cardClubs5.png',
            'Fall25_final_project_weber/assets/Cards/cardClubs6.png','Fall25_final_project_weber/assets/Cards/cardClubs7.png',
            'Fall25_final_project_weber/assets/Cards/cardClubs8.png','Fall25_final_project_weber/assets/Cards/cardClubs9.png',
            'Fall25_final_project_weber/assets/Cards/cardClubs10.png','Fall25_final_project_weber/assets/Cards/cardClubsA.png',
            'Fall25_final_project_weber/assets/Cards/cardClubsJ.png','Fall25_final_project_weber/assets/Cards/cardClubsK.png',
            'Fall25_final_project_weber/assets/Cards/cardClubsQ.png'
            ]
        self.pick_card = choice(self.cards)
        self.image = pygame.image.load(self.pick_card)
        self.rect = self.image.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (x,y)

    def draw(self, screen):
        screen.blit(self.image,self.rect)
