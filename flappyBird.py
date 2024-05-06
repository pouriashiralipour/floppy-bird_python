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

# LOAD IMAGES
background_image = pygame.transform.scale2x(
    pygame.image.load(variables.BACKGROUND_IMAGE_ADDRESS)
)
floor_image = pygame.transform.scale2x(pygame.image.load(variables.FLOOR_IMAGE_ADDRESS))
# GAME TIMER
clock = pygame.time.Clock()

# GMAE LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            sys.exit()
    # SHOW BACKGROUND ON MAINSCREEN
    main_screen.blit(background_image, (0, 0))
    # SHOW FLOOR ON MAINSCREEN
    main_screen.blit(floor_image, (variables.FLOOR_X, 800))
    variables.FLOOR_X -= 1
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(variables.CLOCK_TIME)
