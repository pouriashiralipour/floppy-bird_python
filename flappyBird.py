# instagram : @pouria.shirali

import sys

import pygame
import pygame.locals

# GLOBAL VARIABLES
import variables

# GAME DISPLAY
main_screen = pygame.display.set_mode(
    (variables.display_with, variables.display_height)
)
# START PYGAME MODULES
pygame.init()

# LOAD IMAGES
background_image = pygame.transform.scale2x(
    pygame.image.load(variables.background_image_address)
)
floor_image = pygame.transform.scale2x(pygame.image.load(variables.floor_image_address))
bird_image = pygame.transform.scale2x(pygame.image.load(variables.bird_image))
pip_image = pygame.transform.scale2x(pygame.image.load(variables.pipe_image))

# RECTANGLE FOR BIRD
bird_image_ractangle = bird_image.get_rect(center=(100, variables.display_height / 2))

# GAME TIMER
clock = pygame.time.Clock()

# GMAE LOGIC
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            # END PYGAME MODULES
            pygame.quit()
            sys.exit()
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                variables.bird_movement = 0
                variables.bird_movement -= 8
    # SHOW BACKGROUND ON MAINSCREEN
    main_screen.blit(background_image, (0, 0))
    # SHOW BIRD IMAGE
    main_screen.blit(bird_image, bird_image_ractangle)
    # FLOOR GRAVITY & BIRD MOVEMENT
    variables.bird_movement += variables.gravity
    bird_image_ractangle.centery += variables.bird_movement
    # SHOW FLOOR ON MAINSCREEN
    variables.floor_x -= 1
    main_screen.blit(floor_image, (variables.floor_x, variables.display_height - 150))
    main_screen.blit(
        floor_image,
        (variables.floor_x + variables.display_with, variables.display_height - 150),
    )

    if variables.floor_x <= -variables.display_with:
        variables.floor_x = 0
    pygame.display.update()
    # SET GAME SPEED
    clock.tick(variables.clock_time)
