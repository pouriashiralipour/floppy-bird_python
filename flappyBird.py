# instagram : @pouria.shirali

import sys

import pygame

pygame.init()

# create main screen with favorite size
main_screen = pygame.display.set_mode((576, 980))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
