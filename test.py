import pygame
from sys import exit

def display_score():
    current_time = (pygame.time.get_ticks() - start_time) // 1000
    score_surface = test_font.render(f"Score : {current_time}", False, (64, 64, 64))
    score_rectangle = score_surface.get_rect(center = (400, 50))
    screen.blit(score_surface, score_rectangle)
    return current_time
    

pygame.init()

screen = pygame.display.set_mode((800, 400))
pygame.display.set_caption('Runner')
clock = pygame.time.Clock()
test_font = pygame.font.Font("font\Pixeltype.ttf", 50)

# test_surface = pygame.Surface((100, 200))
# test_surface.fill("Red")

sky_surface = pygame.image.load("graphics\Sky.png").convert()
ground_suface = pygame.image.load("graphics\ground.png").convert()

score_surface = test_font.render("My game", False, (64, 64, 64))
score_rectangle = score_surface.get_rect(center = (400, 50))

snail_surface = pygame.image.load("graphics\snail\snail1.png").convert_alpha()
snail_rectangle = snail_surface.get_rect(bottomright = (800, 300))

player_surface = pygame.image.load("graphics\player\player_walk_1.png").convert_alpha()
player_rectangle = player_surface.get_rect(bottomleft = (80, 300))

player_stand = pygame.image.load("graphics\player\player_stand.png").convert_alpha()
player_stand = pygame.transform.rotozoom(player_stand, 0, 2)
player_stand_rectangele = player_stand.get_rect(center = (400, 200))

restart_message_surface = test_font.render("Press Space to Continue", False, (111, 196, 169))
restart_message_surface_rectangle = restart_message_surface.get_rect(center = (400, 350))

player_gravity = 0

game_active = True
start_time = 0

while True:
    
    for event in pygame.event.get():
        if (event.type == pygame.QUIT):
            pygame.quit()
            exit()

        elif (event.type == pygame.KEYDOWN and game_active):

            if (event.key == pygame.K_SPACE and player_rectangle.bottom == 300):
                player_gravity = -20

        elif (event.type == pygame.MOUSEBUTTONDOWN and game_active):
            
            if (player_rectangle.collidepoint(event.pos) and player_rectangle.bottom == 300):
                player_gravity = -20

        elif (event.type == pygame.KEYDOWN and not game_active):

            if (event.key == pygame.K_SPACE):
                snail_rectangle.right = 800
                game_active = True
                start_time = pygame.time.get_ticks()
    
    if (game_active):
        screen.blit(sky_surface, (0, 0))
        screen.blit(ground_suface, (0, 300))

        # pygame.draw.rect(screen, "#c0e8ec", score_rectangle)
        # pygame.draw.rect(screen, "#c0e8ec", score_rectangle, 10)
        # screen.blit(score_surface, score_rectangle)
        
        # pygame.draw.line(screen, "Gold", (0, 0), pygame.mouse.get_pos(), 10)
        # pygame.draw.ellipse(screen, "Brown", pygame.Rect(50, 200, 100, 100))

        snail_rectangle.left -= 7
        if (snail_rectangle.right < -100):
            snail_rectangle.right = 800
        
        screen.blit(snail_surface, snail_rectangle)

        # Player

        screen.blit(player_surface, player_rectangle)
        player_gravity += 1
        player_rectangle.y += player_gravity
        if (player_rectangle.bottom >= 300):
            player_rectangle.bottom = 300

        # Collisions

        if(player_rectangle.colliderect(snail_rectangle)):
            game_active = False

        # keys = pygame.key.get_pressed()
        # if keys[pygame.K_SPACE]:
        #     print("jump")

        # mouse_position = pygame.mouse.get_pos()
        # if (player_rectangle.collidepoint(mouse_position)):
        #     print(pygame.mouse.get_pressed())

        final_score = display_score()
    
    else:
        screen.fill((94, 129, 162))
        screen.blit(player_stand, player_stand_rectangele)
        
        final_score_surface = test_font.render(f"Total Score : {final_score}", False, (111, 196, 169))
        final_score_surface_rectangle = final_score_surface.get_rect(center = (400, 70))
        screen.blit(final_score_surface, final_score_surface_rectangle)


        screen.blit(restart_message_surface, restart_message_surface_rectangle)


    pygame.display.update()
    clock.tick(60)


# 2:24:00