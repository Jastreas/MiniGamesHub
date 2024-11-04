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

##Outer Rectangle
outerRectangle_top = pygame.Rect(282, 0, 564, 20)
outerRectangle_left = pygame.Rect(282, 0, 10, 634)
outerRectangle_right = pygame.Rect(846, 0, 10, 634)
outerRectangle_overlay_left = pygame.Rect(282, 550, 10, 20)
outerRectangle_overlay_right = pygame.Rect(846, 550, 10, 20)


#GAME METHODS

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
        self.velocity = pygame.Vector2(2, 2)
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

##1st Brick Line
###x increments in Brick width (137) + separation (2)
###x decrements in Brick height (20) + separation (2)
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
    ##check collision with bottom screen
    if b1.position.y >= screen_Height - b1.radius:
        b1.move(True)
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
    ##1st brick layer
    yellow_b1.spawn(screen)
    yellow_b2.spawn(screen)
    yellow_b3.spawn(screen)
    yellow_b4.spawn(screen)
    ##2nd brick layer
    yellow_b5.spawn(screen)
    yellow_b6.spawn(screen)
    yellow_b7.spawn(screen)
    yellow_b8.spawn(screen)
    ##ball
    b1.paint(screen)

    #FLIP
    pygame.display.flip()
    
    #Limit to 60fps
    dt = clock.tick(60) / 1000

    #debug
    print(score_total)
    #print(player_hitcorner)

pygame.quit()