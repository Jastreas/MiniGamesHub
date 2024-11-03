import pygame

#PYGAME SETUP
pygame.init()
##screen
screen_Width = 1128
screen_Height = 634
screen = pygame.display.set_mode((screen_Width, screen_Height))
pygame.display.set_caption("Astras Breakout")
##clock
clock = pygame.time.Clock()
##game loop
run = True

#MY VARS
##Score
score_total = 0

##player
rect_width = 70
rect_height = 20
dt = 0
###position
player_position = pygame.Vector2((screen_Width / 2) - (rect_width  / 2), 550)
###debug
player_hitcorner = False

##Ball
###position
ball_position = pygame.Vector2((screen_Width / 2), 350)

##Outer Rectangle
outerRectangle_top = pygame.Rect(282, 0, 564, 20)
outerRectangle_left = pygame.Rect(282, 0, 10, 634)
outerRectangle_right = pygame.Rect(846, 0, 10, 634)
outerRectangle_overlay_left = pygame.Rect(282, 550, 10, 20)
outerRectangle_overlay_right = pygame.Rect(846, 550, 10, 20)


while run:

    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        
    
    #Initializing Player
    player = pygame.Rect(player_position.x, player_position.y, rect_width, rect_height)

    #playerMovement
    key = pygame.key.get_pressed()
    player_speed = 600 * dt

    if key[pygame.K_a] and player_position.x >= 292: #282 + 10 
        player_position.x -= player_speed
    if key[pygame.K_d] and player_position.x <= 846 - rect_width: 
        player_position.x += player_speed

    #ballMovement
    
    

    #GAME RENDER
    screen.fill("black")
    pygame.draw.rect(screen, "white", outerRectangle_top)
    pygame.draw.rect(screen, "white", outerRectangle_left)
    pygame.draw.rect(screen, "white", outerRectangle_right)
    pygame.draw.rect(screen, "blue", outerRectangle_overlay_left)
    pygame.draw.rect(screen, "blue", outerRectangle_overlay_right)
    pygame.draw.rect(screen, "blue", player)
    pygame.draw.circle(screen, "gray", ball_position, 5)

    #FLIP
    pygame.display.flip()
    
    #Limit to 60fps
    dt = clock.tick(60) / 1000

    #debug
    #print(player_hitcorner)

pygame.quit()