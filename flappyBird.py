# instagram : @pouria.shirali

import sys

import pygame

# GLOBAL VARIABLES
import variables

# GAME DISPLAY
main_screen = pygame.display.set_mode(
    (variables.DISPLAY_WITH, variables.DISPLAY_HEIGHT)
)
# START PYGAME MODULES
pygame.init()

# GAME TIMER
clock = pygame.time.Clock()

# GMAE LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            sys.exit()
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(variables.CLOCK_TIME)
