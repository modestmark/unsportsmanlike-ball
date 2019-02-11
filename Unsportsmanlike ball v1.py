#This is the initial framework code for a sportsball like game

import sys, pygame




pygame.init()

clockobject = pygame.time.Clock()
keys=pygame.key.get_pressed()

size = width, height = 600, 400

speedx = 0
speedz = 0

float (speedx)
float (speedz)


black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("BirdDemo4.png")
ballrect = ball.get_rect()

#This is the main loop

while 1:

    clockobject.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    events = pygame.event.get()
    
    ballrect = ballrect.move(speedx, speedz)

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT and speedx > -7:
                speedx = speedx -1
            if event.key == pygame.K_RIGHT and speedx < 7:
                speedx = speedx + 1
            if event.key == pygame.K_UP and speedz >  -6:
                speedz = speedz - 3
            if event.key == pygame.K_DOWN:
                speedz = speedz + 1


#Bounding

    if ballrect.left < 0:
        speedx = +2
    if ballrect.right > width:
        speedx = -2
    if ballrect.top < 0:
        speedz = +2
    if ballrect.bottom > height:
        speedz = -2


#Advanced Gravity Simulation
    if speedz < 1:

        speedz = speedz + 20




    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
