import pygame

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
run = True
green = (45, 120, 45)
gray = (20, 20, 20)
dt = 0
speed = 20
playerPosition = pygame.Vector2(500, 500)


#CLASSES
class player_Square:
    def __init__(self):
        self.Position = playerPosition
        self.rect = pygame.Rect(self.Position.x, self.Position.y, 30, 30)
    def spawn(self, screen):
        pygame.draw.rect(screen, gray, self.rect)
    #def playermove(self, key):
        #if key[pygame.K_a]:
            #print(self.playerPosition.x)

def player_AutoMove(speedv, axis):
    axis += speedv


while run:

    p1 = player_Square()
    if speed < 20:
        speed += 200 * dt

    playerPosition.x += speed


    #MOVEMENT
    key = pygame.key.get_pressed()



    # RENDER YOUR GAME HERE
    screen.fill(green)
    p1.spawn(screen)


    #Rest of stuff
    pygame.display.flip()
    dt = clock.tick(30) / 1000


    #Event Handler
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    #DEBUG


pygame.quit()