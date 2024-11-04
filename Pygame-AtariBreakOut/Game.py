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
pause = True

##player
player_hp = 3
rect_width = 70
rect_height = 20
dt = 0
player_lastChance = True
###position
player_position = pygame.Vector2((screen_Width / 2) - (rect_width  / 2), 550)
###debug
player_hitcorner = False

##Outer Rectangle
outerRectangle_top = pygame.Rect(282, 0, 564, 20)
outerRectangle_left = pygame.Rect(282, 0, 10, 634)
outerRectangle_right = pygame.Rect(846, 0, 10, 634)
outerRectangle_overlay_left = pygame.Rect(282, 550, 10, 20)
outerRectangle_overlay_right = pygame.Rect(846, 550, 10, 20)

#Text properties
font = pygame.font.SysFont('CozetteVector', 60)
white = (255, 255, 255)
red = (255, 0, 0)


#GAME METHODS
def draw_text(text, font, text_col, x, y):
    img = font.render(text, True, text_col)
    screen.blit(img, (x, y))

#CLASSES
class Brick:
    def __init__(self, pos_x, pos_y, color, hp):
        self.rect = pygame.Rect(pos_x, pos_y, 137, 20)
        self.color = color
        self.hp = hp
        self.isDestroyed = False
    def spawn(self, screen):
        if self.hp > 0:
            pygame.draw.rect(screen, self.color, self.rect)
        else:
            self.isDestroyed = True

##Ball
###position
ball_position = pygame.Vector2((screen_Width / 2), 450)

class Ball:
    def __init__(self, position, color):
        self.position = ball_position
        self.color = color
        self.radius = 5
        self.velocity = pygame.Vector2(5, 5)
        self.moving = True

    def move(self, stop):
        if stop:
            moving = False
        else:
            moving = True
        
        if moving:
            self.position += self.velocity
        else:
            self.position += self.velocity * 0
            
    def paint(self, screen):
        pygame.draw.circle(screen, self.color, (int (self.position.x), int (self.position.y)), self.radius)


#ASSET GROUPS

##Ball
b1 = Ball(ball_position, "gray")
b1_bounces = 0

###x increments in Brick width (137) + separation (2)
###y decrements in Brick height (20) + separation (2)
##Yellow Brick Line
yellow_score = 10
yellow_b1 = Brick(292, 250, "yellow", 1)
b1_gave = False
yellow_b2 = Brick(431, 250, "yellow", 1)
b2_gave = False
yellow_b3 = Brick(570, 250, "yellow", 1)
b3_gave = False
yellow_b4 = Brick(709, 250, "yellow", 1)
b4_gave = False
yellow_b5 = Brick(292, 228, "yellow", 1)
b5_gave = False
yellow_b6 = Brick(431, 228, "yellow", 1)
b6_gave = False
yellow_b7 = Brick(570, 228, "yellow", 1)
b7_gave = False
yellow_b8 = Brick(709, 228, "yellow", 1)
b8_gave = False

##Green Brick Line
green_score = 20
green_b1 = Brick(292, 206, "green", 2)
gb1_gave = False
green_b2 = Brick(431, 206, "green", 2)
gb2_gave = False
green_b3 = Brick(570, 206, "green", 2)
gb3_gave = False
green_b4 = Brick(709, 206, "green", 2)
gb4_gave = False
green_b5 = Brick(292, 184, "green", 2)
gb5_gave = False
green_b6 = Brick(431, 184, "green", 2)
gb6_gave = False
green_b7 = Brick(570, 184, "green", 2)
gb7_gave = False
green_b8 = Brick(709, 184, "green", 2)
gb8_gave = False

##Red Brick Line
red_score = 40
red_b1 = Brick(292, 162, "red", 4)
rb1_gave = False
red_b2 = Brick(431, 162, "red", 4)
rb2_gave = False
red_b3 = Brick(570, 162, "red", 4)
rb3_gave = False
red_b4 = Brick(709, 162, "red", 4)
rb4_gave = False
red_b5 = Brick(292, 140, "red", 4)
rb5_gave = False
red_b6 = Brick(431, 140, "red", 4)
rb6_gave = False
red_b7 = Brick(570, 140, "red", 4)
rb7_gave = False
red_b8 = Brick(709, 140, "red", 4)
rb8_gave = False

##Orange Brick Line
orange_score = 80
orange_b1 = Brick(292, 118, "orange", 6)
ob1_gave = False
orange_b2 = Brick(431, 118, "orange", 6)
ob2_gave = False
orange_b3 = Brick(570, 118, "orange", 6)
ob3_gave = False
orange_b4 = Brick(709, 118, "orange", 6)
ob4_gave = False
orange_b5 = Brick(292, 96, "orange", 6)
ob5_gave = False
orange_b6 = Brick(431, 96, "orange", 6)
ob6_gave = False
orange_b7 = Brick(570, 96, "orange", 6)
ob7_gave = False
orange_b8 = Brick(709, 96, "orange", 6)
ob8_gave = False

while run:
    
    #Initializing Player
    player = pygame.Rect(player_position.x, player_position.y, rect_width, rect_height)

    #playerMovement
    key = pygame.key.get_pressed()
    player_speed = 600 * dt

    if player_hp > 0 or player_lastChance:
        if key[pygame.K_a] and player_position.x >= 292: #282 + 10 
            player_position.x -= player_speed
        if key[pygame.K_d] and player_position.x <= 846 - rect_width: 
            player_position.x += player_speed

        #ballMovement
        ##make ball faster when counter get to 0 and reset
        if b1_bounces == 4:
            b1.velocity *= 1.15
            b1_bounces = 0

    ##check collision with bottom screen
    if b1.position.y >= screen_Height - b1.radius:
        if player_hp > 0:
            b1.position.x = screen_Width / 2
            b1.position.y = 450
            player_hp -= 1
            b1.velocity.x = 5
            b1.velocity.y = 5
        else: #this means player has lost all 3 chances
            b1.move(True)
            player_lastChance = False
    else:
        b1.move(False)

    ##check collision with right outer rectangle
    if outerRectangle_right.collidepoint(b1.position):
        b1.velocity.x *= -1
    if outerRectangle_left.collidepoint(b1.position):
        b1.velocity.x *= -1
    if outerRectangle_top.collidepoint(b1.position):
        b1.velocity.y *= -1
        b1.position.y = outerRectangle_top.bottom + b1.radius

    ##check collision with player
    if player.collidepoint(b1.position):
        b1.velocity.y *= -1
        b1.position.y = player.top - b1.radius
        b1_bounces += 1

    ##check collision with yellow bricks
    ###B1
    if yellow_b1.rect.collidepoint(b1.position) and not yellow_b1.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b1.rect.bottom + b1.radius
        yellow_b1.hp -= 1
    if yellow_b1.isDestroyed and not b1_gave:
        score_total += yellow_score
        b1_gave = True
    ###B2
    if yellow_b2.rect.collidepoint(b1.position) and not yellow_b2.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b2.rect.bottom + b1.radius
        yellow_b2.hp -= 1
    if yellow_b2.isDestroyed and not b2_gave:
        score_total += yellow_score
        b2_gave = True
    ###B3
    if yellow_b3.rect.collidepoint(b1.position) and not yellow_b3.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b3.rect.bottom + b1.radius
        yellow_b3.hp -= 1
    if yellow_b3.isDestroyed and not b3_gave:
        score_total += yellow_score
        b3_gave = True
    ###B4
    if yellow_b4.rect.collidepoint(b1.position) and not yellow_b4.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b4.rect.bottom + b1.radius
        yellow_b4.hp -= 1
    if yellow_b4.isDestroyed and not b4_gave:
        score_total += yellow_score
        b4_gave = True
    ###B5
    if yellow_b5.rect.collidepoint(b1.position) and not yellow_b5.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b5.rect.bottom + b1.radius
        yellow_b5.hp -= 1
    if yellow_b5.isDestroyed and not b5_gave:
        score_total += yellow_score
        b5_gave = True
    ###B6
    if yellow_b6.rect.collidepoint(b1.position) and not yellow_b6.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b6.rect.bottom + b1.radius
        yellow_b6.hp -= 1
    if yellow_b6.isDestroyed and not b6_gave:
        score_total += yellow_score
        b6_gave = True
    ###B7
    if yellow_b7.rect.collidepoint(b1.position) and not yellow_b7.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b7.rect.bottom + b1.radius
        yellow_b7.hp -= 1
    if yellow_b7.isDestroyed and not b7_gave:
        score_total += yellow_score
        b7_gave = True
    ###B8
    if yellow_b8.rect.collidepoint(b1.position) and not yellow_b8.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = yellow_b8.rect.bottom + b1.radius
        yellow_b8.hp -= 1
    if yellow_b8.isDestroyed and not b8_gave:
        score_total += yellow_score
        b8_gave = True

    ##check collision with green bricks
    ###B1
    if green_b1.rect.collidepoint(b1.position) and not green_b1.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b1.rect.bottom + b1.radius
        green_b1.hp -= 1
    if green_b1.isDestroyed and not gb1_gave:
        score_total += green_score
        gb1_gave = True
    ###B2
    if green_b2.rect.collidepoint(b1.position) and not green_b2.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b2.rect.bottom + b1.radius
        green_b2.hp -= 1
    if green_b2.isDestroyed and not gb2_gave:
        score_total += green_score
        gb2_gave = True
    ###B3
    if green_b3.rect.collidepoint(b1.position) and not green_b3.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b3.rect.bottom + b1.radius
        green_b3.hp -= 1
    if green_b3.isDestroyed and not gb3_gave:
        score_total += green_score
        gb3_gave = True
    ###B4
    if green_b4.rect.collidepoint(b1.position) and not green_b4.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b4.rect.bottom + b1.radius
        green_b4.hp -= 1
    if green_b4.isDestroyed and not gb4_gave:
        score_total += green_score
        gb4_gave = True
    ###B5
    if green_b5.rect.collidepoint(b1.position) and not green_b5.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b5.rect.bottom + b1.radius
        green_b5.hp -= 1
    if green_b5.isDestroyed and not gb5_gave:
        score_total += green_score
        gb5_gave = True
    ###B6
    if green_b6.rect.collidepoint(b1.position) and not green_b6.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b6.rect.bottom + b1.radius
        green_b6.hp -= 1
    if green_b6.isDestroyed and not gb6_gave:
        score_total += green_score
        gb6_gave = True
    ###B7
    if green_b7.rect.collidepoint(b1.position) and not green_b7.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b7.rect.bottom + b1.radius
        green_b7.hp -= 1
    if green_b7.isDestroyed and not gb7_gave:
        score_total += green_score
        gb7_gave = True
    ###B8
    if green_b8.rect.collidepoint(b1.position) and not green_b8.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = green_b8.rect.bottom + b1.radius
        green_b8.hp -= 1
    if green_b8.isDestroyed and not gb8_gave:
        score_total += green_score
        gb8_gave = True

##check collision with red bricks
    ###B1
    if red_b1.rect.collidepoint(b1.position) and not red_b1.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b1.rect.bottom + b1.radius
        red_b1.hp -= 1
    if red_b1.isDestroyed and not rb1_gave:
        score_total += red_score
        rb1_gave = True
    ###B2
    if red_b2.rect.collidepoint(b1.position) and not red_b2.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b2.rect.bottom + b1.radius
        red_b2.hp -= 1
    if red_b2.isDestroyed and not rb2_gave:
        score_total += red_score
        rb2_gave = True
    ###B3
    if red_b3.rect.collidepoint(b1.position) and not red_b3.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b3.rect.bottom + b1.radius
        red_b3.hp -= 1
    if red_b3.isDestroyed and not rb3_gave:
        score_total += red_score
        rb3_gave = True
    ###B4
    if red_b4.rect.collidepoint(b1.position) and not red_b4.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b4.rect.bottom + b1.radius
        red_b4.hp -= 1
    if red_b4.isDestroyed and not rb4_gave:
        score_total += red_score
        rb4_gave = True
    ###B5
    if red_b5.rect.collidepoint(b1.position) and not red_b5.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b5.rect.bottom + b1.radius
        red_b5.hp -= 1
    if red_b5.isDestroyed and not rb5_gave:
        score_total += red_score
        rb5_gave = True
    ###B6
    if red_b6.rect.collidepoint(b1.position) and not red_b6.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b6.rect.bottom + b1.radius
        red_b6.hp -= 1
    if red_b6.isDestroyed and not rb6_gave:
        score_total += red_score
        rb6_gave = True
    ###B7
    if red_b7.rect.collidepoint(b1.position) and not red_b7.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b7.rect.bottom + b1.radius
        red_b7.hp -= 1
    if red_b7.isDestroyed and not rb7_gave:
        score_total += red_score
        rb7_gave = True
    ###B8
    if red_b8.rect.collidepoint(b1.position) and not red_b8.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = red_b8.rect.bottom + b1.radius
        red_b8.hp -= 1
    if red_b8.isDestroyed and not rb8_gave:
        score_total += red_score
        rb8_gave = True
    ##check collision with orange bricks
    ###B1
    if orange_b1.rect.collidepoint(b1.position) and not orange_b1.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b1.rect.bottom + b1.radius
        orange_b1.hp -= 1
    if orange_b1.isDestroyed and not ob1_gave:
        score_total += orange_score
        ob1_gave = True
    ###B2
    if orange_b2.rect.collidepoint(b1.position) and not orange_b2.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b2.rect.bottom + b1.radius
        orange_b2.hp -= 1
    if orange_b2.isDestroyed and not ob2_gave:
        score_total += orange_score
        ob2_gave = True
    ###B3
    if orange_b3.rect.collidepoint(b1.position) and not orange_b3.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b3.rect.bottom + b1.radius
        orange_b3.hp -= 1
    if orange_b3.isDestroyed and not ob3_gave:
        score_total += orange_score
        ob3_gave = True
    ###B4
    if orange_b4.rect.collidepoint(b1.position) and not orange_b4.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b4.rect.bottom + b1.radius
        orange_b4.hp -= 1
    if orange_b4.isDestroyed and not ob4_gave:
        score_total += orange_score
        ob4_gave = True
    ###B5
    if orange_b5.rect.collidepoint(b1.position) and not orange_b5.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b5.rect.bottom + b1.radius
        orange_b5.hp -= 1
    if orange_b5.isDestroyed and not ob5_gave:
        score_total += orange_score
        ob5_gave = True
    ###B6
    if orange_b6.rect.collidepoint(b1.position) and not orange_b6.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b6.rect.bottom + b1.radius
        orange_b6.hp -= 1
    if orange_b6.isDestroyed and not ob6_gave:
        score_total += orange_score
        ob6_gave = True
    ###B7
    if orange_b7.rect.collidepoint(b1.position) and not orange_b7.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b7.rect.bottom + b1.radius
        orange_b7.hp -= 1
    if orange_b7.isDestroyed and not ob7_gave:
        score_total += orange_score
        ob7_gave = True
    ###B8
    if orange_b8.rect.collidepoint(b1.position) and not orange_b8.isDestroyed:
        b1.velocity.y *= -1
        b1.position.y = orange_b8.rect.bottom + b1.radius
        orange_b8.hp -= 1
    if orange_b8.isDestroyed and not ob8_gave:
        score_total += orange_score
        ob8_gave = True

    #GAME RENDER
    screen.fill("black")
    ##border
    pygame.draw.rect(screen, "white", outerRectangle_top)
    pygame.draw.rect(screen, "white", outerRectangle_left)
    pygame.draw.rect(screen, "white", outerRectangle_right)
    pygame.draw.rect(screen, "blue", outerRectangle_overlay_left)
    pygame.draw.rect(screen, "blue", outerRectangle_overlay_right)
    ##player
    pygame.draw.rect(screen, "blue", player)
    ##Yellow brick layer
    yellow_b1.spawn(screen)
    yellow_b2.spawn(screen)
    yellow_b3.spawn(screen)
    yellow_b4.spawn(screen)
    yellow_b5.spawn(screen)
    yellow_b6.spawn(screen)
    yellow_b7.spawn(screen)
    yellow_b8.spawn(screen)
    ##Red brick layer
    green_b1.spawn(screen)
    green_b2.spawn(screen)
    green_b3.spawn(screen)
    green_b4.spawn(screen)
    green_b5.spawn(screen)
    green_b6.spawn(screen)
    green_b7.spawn(screen)
    green_b8.spawn(screen)
    ##Red brick layer
    red_b1.spawn(screen)
    red_b2.spawn(screen)
    red_b3.spawn(screen)
    red_b4.spawn(screen)
    red_b5.spawn(screen)
    red_b6.spawn(screen)
    red_b7.spawn(screen)
    red_b8.spawn(screen)
    ##Orange brick layer
    orange_b1.spawn(screen)
    orange_b2.spawn(screen)
    orange_b3.spawn(screen)
    orange_b4.spawn(screen)
    orange_b5.spawn(screen)
    orange_b6.spawn(screen)
    orange_b7.spawn(screen)
    orange_b8.spawn(screen)

    ##Draw score
    draw_text(str(score_total), font, white, screen_Width/2 - 18, 20)

    ##Draw game over message
    if player_hp == 0 and not player_lastChance:
        draw_text("You Lost", font, red, screen_Width / 2 - 100, screen_Height / 2 )

    if pause:
        draw_text("PAUSED", font, red, screen_Width // 2 - 100, screen_Height // 2 - 30)

    ##ball
    b1.paint(screen)

    #FLIP
    pygame.display.flip()
    
    #Limit to 60fps
    dt = clock.tick(60) / 1000

    #EVENT HANDLER
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
        # Detecta si se presiona la tecla de pausa (p)
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_p:  # Cambia el estado de pausa con la tecla P
                pause = not pause

    #debug
        #print(b1_bounces)
        #print(score_total)
        #print(player_hitcorner)
    print(pause)

pygame.quit()