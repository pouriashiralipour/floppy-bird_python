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
            variables.active_score = True
            return False
        if (
            bird_image_ractangle.top <= -50
            or bird_image_ractangle.bottom >= variables.display_height - 150
        ):
            return False
    return True


# DISPLAY SCORE
def display_score(status):
    if status == "active":
        score_text = gmae_font.render(f"{variables.score}", False, (255, 255, 255))
        score_text_rectangle = score_text.get_rect(center=(288, 100))
        main_screen.blit(score_text, score_text_rectangle)
    if status == "not_active":
        # SCORE
        score_text = gmae_font.render(
            f"Score: {variables.score}", False, (255, 255, 255)
        )
        score_text_rectangle = score_text.get_rect(center=(288, 100))
        main_screen.blit(score_text, score_text_rectangle)
        # HIGH SCORE
        high_score_text = gmae_font.render(
            f"HiGh Score: {variables.high_score}", False, (229, 20, 20)
        )
        high_score_text_rectangle = high_score_text.get_rect(center=(288, 800))
        main_screen.blit(high_score_text, high_score_text_rectangle)


# UPDATE SCORE
def update_score():
    if variables.pipe_list:
        for pipe in variables.pipe_list:
            if 98 < pipe.centerx < 102 and variables.active_score:
                variables.score += 1
                variables.active_score = False
            if pipe.centerx < 0:
                variables.active_score = True
    if variables.score > variables.high_score:
        variables.high_score = variables.score
    return variables.high_score


# BIRD ANIMATION
def bird_animation():
    new_bird_image = birds_list[variables.bird_list_index]
    new_bird_imgae_rectangle = new_bird_image.get_rect(
        center=(100, bird_image_ractangle.centery)
    )
    return new_bird_image, new_bird_imgae_rectangle


# GAME DISPLAY
main_screen = pygame.display.set_mode(
    (variables.display_with, variables.display_height)
)
# LOAD FONT
gmae_font = pygame.font.Font(variables.game_font, 40)

# LOAD IMAGES
background_image = pygame.transform.scale2x(
    pygame.image.load(variables.background_image_address)
)
floor_image = pygame.transform.scale2x(pygame.image.load(variables.floor_image_address))

pip_image = pygame.transform.scale2x(pygame.image.load(variables.pipe_image))
bird_image_middle = pygame.transform.scale2x(pygame.image.load(variables.bird_image))
bird_image_top = pygame.transform.scale2x(pygame.image.load(variables.bird_top_image))
bird_image_down = pygame.transform.scale2x(
    pygame.image.load(variables.bird_bottom_image)
)
# CREATE LIST FOR BIRDS
birds_list = [bird_image_down, bird_image_middle, bird_image_top]
bird_image = birds_list[variables.bird_list_index]
# USER EVENTS
# CREATE PIPE
create_pipe = pygame.USEREVENT
pygame.time.set_timer(create_pipe, 1200)
# CREATE TRANSITION FOR BIRD
create_flap = pygame.USEREVENT + 1
pygame.time.set_timer(create_flap, 100)
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
            if event.key == pygame.K_r and variables.game_status == False:
                variables.game_status = True
                variables.pipe_list.clear()
                bird_image_ractangle.center = 100, variables.display_height / 2
                variables.bird_movement = 0
                variables.score = 0
        if event.type == create_pipe:
            variables.pipe_list.extend(generate_pipe_rectangle())
        if event.type == create_flap:
            if variables.bird_list_index < 2:
                variables.bird_list_index += 1
            else:
                variables.bird_list_index = 0
            bird_image, bird_image_ractangle = bird_animation()
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
        # SHOW SCORE
        update_score()
        display_score("active")
    else:
        display_score("not_active")
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
