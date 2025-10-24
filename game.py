# Example file showing a basic pygame "game loop"
import pygame
from random import randint
from util_params import *
from card import Card
from chips import Chip


# pygame setup
pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGHT))
clock = pygame.time.Clock()
running = True

################### Testing Zone ###################

card_list = [Card(100, 475),Card(100,125)]
chip = Chip(300,500)

####################################################

while running:
    # poll for events
    # pygame.QUIT event means the user clicked X to close your window
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # fill the screen with a color to wipe away anything from last frame
    kelly_green = (10, 134, 61)
    screen.fill(kelly_green)

    # RENDER YOUR GAME HERE
    for card in card_list:
        card.draw(screen)
    chip.draw(screen)

    # flip() the display to put your work on screen
    pygame.display.flip()

    clock.tick(60)  # limits FPS to 60

pygame.quit()