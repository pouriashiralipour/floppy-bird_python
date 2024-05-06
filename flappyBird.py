# instagram : @pouria.shirali

import sys

import pygame
import pygame.locals

# GLOBAL VARIABLES
import variables

# GAME DISPLAY
main_screen = pygame.display.set_mode(
    (variables.DISPLAY_WITH, variables.DISPLAY_HEIGHT)
)
# START PYGAME MODULES
pygame.init()

# LOAD BACKGROUND IMAGE
background_image = pygame.image.load(variables.BACKGROUND_IMAGE_ADDRESS)

# GAME TIMER
clock = pygame.time.Clock()

# GMAE LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            sys.exit()
    # SHOW BACKGROUND
    main_screen.blit(background_image, (0, 0))
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(variables.CLOCK_TIME)
