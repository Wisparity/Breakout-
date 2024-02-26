import pygame
import random
pygame.init()
class brick:
    def __init__(self, xpos, ypos):
        self.xpos = xpos
        self.ypos = ypos
        self.color = (random.randrange(100,250),random.randrange(100,250), random.randrange(100,250))
        self.isDead = False
    def draw(self):
        if not self.isDead:
            pygame.draw.rect(screen, self.color, (self.xpos, self.ypos, 100,50)) #Width and height are 100 and 50 
        #bounding box collision
    def collide(self, ball_x, ball_y):
        if not self.isDead:
            if (ball_x + 20 > self.xpos and
                ball_x < self.xpos + 100 and #Width of brick is 100
                ball_y + 20 > self.ypos and 
                ball_y < self.ypos + 50): #Height of brick is 50
                pygame.mixer.Sound.play(Breaksfx)
                self.isDead = True
                return True
            
screen = pygame.display.set_mode((700,500))
pygame.display.set_caption("Breakout")

doExit = False

Breaksfx = pygame.mixer.Sound("Pop sound effect.mp3")
BgMusic = pygame.mixer.Sound("Portal Radio Tune.mp3")
pygame.mixer.Sound.play(BgMusic)
clock = pygame.time.Clock()
#player variables
p1x = 300
p1y = 450
b1 = brick (50,50)
b2 = brick (200,50)
b3 = brick (350,50)
b4 = brick (500,50)
b5 = brick (50,150)
b6 = brick (200,150)
b7 = brick (350,150)
b8 = brick (500,150)
b9 = brick (50,250)
b10 = brick (200,250)
b11 = brick (350,250)
b12 = brick (500,250)
#Ball Variables
bx = 350
by = 150
bVx = 5
bVy = 5
while not doExit: # Game loop
    
    clock.tick(60) # Fps
    
    for event in pygame.event.get(): #if player made an action 
        if event.type == pygame.QUIT: #check for user clicking close
            doExit = True #Exit game loop
    keys = pygame.key.get_pressed()
    #player key variables
    if keys[pygame.K_a]:
        p1x-=10
    elif keys[pygame.K_d]:
        p1x+=10
    #Ball Velocity
    bx += bVx
    by += bVy
    if bx < 0 or bx + 20 > 700:
        bVx *= -1
    elif by < 0 or by + 20 > 700:
        bVy *= -1
    #Ball Physics
    if bx < p1x + 100 and by + 20 > p1y and by < p1y + 20:
        bVy *= -1
        bVx *= -1
    #ball collion with each brick
    if b1.collide(bx, by):
        bVy *= -1
    if b2.collide(bx, by):
        bVy *= -1
    if b3.collide(bx, by):
        bVy *= -1
    if b4.collide(bx, by) :
        bVy *= -1
    if b5.collide(bx, by):
        bVy *= -1
    if b6.collide(bx, by) :
        bVy *= -1
    if b7.collide(bx, by) :
        bVy *= -1
    if b8.collide(bx, by) :
        bVy *= -1
    if b9.collide(bx, by) :
        bVy *= -1
    if b10.collide(bx, by) :
        bVy *= -1
    if b11.collide(bx, by) :
        bVy *= -1
    if b12.collide(bx, by) :
        bVy *= -1
    
    screen.fill((0,0,0))
    
    pygame.draw.rect(screen, (255,255,255), (p1x,p1y,100,20))
    pygame.draw.rect(screen, (255,255,255), (bx,by,20,20))
    b1.draw() 
    b2.draw()
    b3.draw()
    b4.draw()
    b5.draw()
    b6.draw()
    b7.draw()
    b8.draw()
    b9.draw()
    b10.draw()
    b11.draw()
    b12.draw()
    pygame.display.flip()
    


            
            
            
            
            
pygame.quit()
