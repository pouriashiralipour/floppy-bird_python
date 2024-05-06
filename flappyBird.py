# instagram : @pouria.shirali

import sys

import pygame

import variables

pygame.init()

# create main screen with favorite size
main_screen = pygame.display.set_mode(
    (variables.DISPLAY_WITH, variables.DISPLAY_HEIGHT)
)
clock = pygame.time.Clock()

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    pygame.display.update()
    clock.tick(variables.CLOCK_TIME)
