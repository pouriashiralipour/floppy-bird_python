# instagram : @pouria.shirali

import random
import sys

import pygame
import pygame.locals

# GLOBAL VARIABLES
import variables

# START PYGAME MODULES
pygame.init()


# FUNCTION FOR PIPE
def generate_pipe_rectangle():
    random_pipes = random.randrange(400, 800)
    pipe_rectangle_top = pip_image.get_rect(
        midbottom=(variables.display_with + 200, random_pipes - 300)
    )
    pipe_rectangle_bottom = pip_image.get_rect(
        midtop=(variables.display_with + 200, random_pipes)
    )
    return pipe_rectangle_bottom, pipe_rectangle_top


# FUNCTION FOR MOVEMENT PIPE
def move_pipe_rectangle(pipes):
    for pipe in pipes:
        pipe.centerx -= 5
    inside_pipes = [pipe for pipe in pipes if pipe.right > -50]
    return inside_pipes


# FUNCTION FOR SHOW PIPE IMAGE
def display_pipes(pipes):
    for pipe in pipes:
        if pipe.bottom >= variables.display_height:
            main_screen.blit(pip_image, pipe)
        else:
            reversed_pipes_image = pygame.transform.flip(pip_image, False, True)
            main_screen.blit(reversed_pipes_image, pipe)


# FUNCTION FOR COLLISION ITEMS
def check_collision(pipes):
    for pipe in pipes:
        if bird_image_ractangle.colliderect(pipe):
            return False
        if (
            bird_image_ractangle.top <= -50
            or bird_image_ractangle.bottom >= variables.display_height - 150
        ):
            return False
    return True


# GAME DISPLAY
main_screen = pygame.display.set_mode(
    (variables.display_with, variables.display_height)
)


# LOAD IMAGES
background_image = pygame.transform.scale2x(
    pygame.image.load(variables.background_image_address)
)
floor_image = pygame.transform.scale2x(pygame.image.load(variables.floor_image_address))
bird_image = pygame.transform.scale2x(pygame.image.load(variables.bird_image))
pip_image = pygame.transform.scale2x(pygame.image.load(variables.pipe_image))

# CREATE PIPE
create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1200)

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
                variables.bird_movement -= 6
            if event.type == pygame.K_r and variables.game_status == False:
                variables.game_status = True
                variables.pipe_list.clear()
                bird_image_ractangle.center = 100, variables.display_height / 2
                variables.bird_movement = 0
        if event.type == create_pipe:
            variables.pipe_list.extend(generate_pipe_rectangle())
    # SHOW BACKGROUND ON MAINSCREEN
    main_screen.blit(background_image, (0, 0))
    if variables.game_status:
        # SHOW BIRD IMAGE
        main_screen.blit(bird_image, bird_image_ractangle)
        # CHECK BIRD COLLISION
        variables.game_status = check_collision(variables.pipe_list)
        # MAKE TRANSFORM MOVE FOR PIPES
        variables.pipe_list = move_pipe_rectangle(variables.pipe_list)
        # DIAPLAY PIPES
        display_pipes(variables.pipe_list)
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
