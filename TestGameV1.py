#This is the initial framework code for a sportsball like game

import sys, pygame
pygame.init()

keys=pygame.key.get_pressed()

size = width, height = 600, 400

speedx = .5
speedz = .5

float (speedx)
float (speedz)


black = 0, 0, 0

screen = pygame.display.set_mode(size)
ball = pygame.image.load("intro_ball.gif")
ballrect = ball.get_rect()

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    events = pygame.event.get()
    
    ballrect = ballrect.move(speedx, speedz)
  
    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                speedx = -1
            if event.key == pygame.K_RIGHT:
                speedx =  1

    if ballrect.left < 0 or ballrect.right > width:
        speedx = speedx-1
    if ballrect.top < 0 or ballrect.bottom > height:
        speedy = -speedy

    screen.fill(black)
    screen.blit(ball, ballrect)
    pygame.display.flip()
