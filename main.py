import pygame
from sys import exit
from random import randint

pygame.init()
width = 800
height = 600
screen = pygame.display.set_mode((width, height))
screen.fill((255, 255, 255))
clock = pygame.time.Clock()

background_surface = pygame.image.load("background.png").convert_alpha()

platform_surface = pygame.image.load("platform.png")
platform_surface_rect = platform_surface.get_rect(midbottom = (width//2, height))

ball_suraface = pygame.image.load("ball.png").convert_alpha()
ball_suraface_rect = ball_suraface.get_rect(midbottom = (width//2, height - platform_surface_rect.height))

font = pygame.font.Font("KnightWarrior.otf", 30)

game_over_surface = font.render("GAME OVER!", True,  "Black")
game_over_surface_rect = game_over_surface.get_rect(center = (width//2, height//2 - 25))

game_restart_message_surface = font.render("Press Space bar to restart the game.", True, "Black")
game_restart_message_surface_rect = game_restart_message_surface.get_rect(center = (width//2, height//2 + 25))

r_num = randint(0,1)

if(r_num):
    positive_velocity_x = False
else:
    positive_velocity_x = True

positive_velocity_y = False

platform_right_movement = False
platform_left_movement = False

ball_velocity = 1
ball_velocity_increment = 0.001

platform_velocity = 15

level = 1
score = 0

running = True

while True:

    for event in pygame.event.get():

        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()
        
        elif (event.type == pygame.KEYDOWN):

            if (event.key == pygame.K_RIGHT):
                platform_right_movement = True
            
            elif (event.key == pygame.K_LEFT):
                platform_left_movement = True

            elif (event.key == pygame.K_SPACE):

                if(not running):
                    platform_surface_rect.midbottom = (width//2, height)
                    ball_suraface_rect.midbottom = (width//2, height - platform_surface_rect.height - 5)                  
                    running = True
            

        elif (event.type == pygame.KEYUP):

            if (event.key == pygame.K_RIGHT):
                platform_right_movement = False

            elif (event.key == pygame.K_LEFT):
                platform_left_movement = False

        

    if(running):

        screen.blit(background_surface, (0, 0))
        screen.blit(ball_suraface, ball_suraface_rect)
        screen.blit(platform_surface, platform_surface_rect)

        
        if (positive_velocity_x):
            ball_suraface_rect.x += ball_velocity
        else:
            ball_suraface_rect.x -= ball_velocity

        if (positive_velocity_y):
            ball_suraface_rect.y += ball_velocity
        else:
            ball_suraface_rect.y -= ball_velocity

        if (ball_suraface_rect.right >= width):
            positive_velocity_x = False
        elif (ball_suraface_rect.left <= 0):
            positive_velocity_x = True
        elif (ball_suraface_rect.top <= 0):
            positive_velocity_y = True

        if (ball_suraface_rect.bottom >= height):
            #positive_velocity_y = False
            #score += level
            # pygame.quit()
            # exit()

            running = False
            reset_score = True
        
        ball_velocity += ball_velocity_increment

        if (platform_right_movement and platform_surface_rect.right < width):
            platform_surface_rect.x += platform_velocity
        elif (platform_left_movement and platform_surface_rect.left > 0):
            platform_surface_rect.x -= platform_velocity
        
        if (ball_suraface_rect.colliderect(platform_surface_rect)):
            positive_velocity_y = False
            score += level

        level = int(ball_velocity)
        level_message_surface = font.render(f"Level : {level}", True, "Black")
        level_message_surface_rect = level_message_surface.get_rect(topleft = (5, 5))
        screen.blit(level_message_surface, level_message_surface_rect)

        if(not running):
            ball_velocity = 1
            score = -1

        score_message_surface = font.render(f"Score : {score}", True, "Black")
        score_message_surface_rect = score_message_surface.get_rect(topright = (width - 5, 5))
        screen.blit(score_message_surface, score_message_surface_rect)

    else:
        screen.blit(background_surface, (0, 0))
        screen.blit(game_over_surface, game_over_surface_rect)
        screen.blit(game_restart_message_surface, game_restart_message_surface_rect)
        
    clock.tick(60)    
    pygame.display.update()
