#!/bin/python3
#This is the initial framework code for a sportsball like game

import sys, pygame
from Birds import Bird




pygame.init()

clockobject = pygame.time.Clock()
keys=pygame.key.get_pressed()

size = width, height = 600, 400


black = 0, 0, 0

screen = pygame.display.set_mode(size)
bird = Bird()

#This is the main loop

while 1:

    clockobject.tick(30)
    for event in pygame.event.get():
        if event.type == pygame.QUIT: sys.exit()
    events = pygame.event.get()
    

    if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT :
                bird.control(-1, 0)
            if event.key == pygame.K_RIGHT :
                bird.control(1, 0)
            if event.key == pygame.K_UP :
                bird.control(0, -5)
            if event.key == pygame.K_DOWN :
                bird.control(0, 1)


#Bounding

    if bird.rect.left < 0:
        bird.speedx = +2
    if bird.rect.right > width:
        bird.speedx = -2
    if bird.rect.top < 0:
        bird.speedz = +2
    if (bird.rect.bottom > height) and (bird.speedz > 0):
        bird.speedz = -2



    print(bird.speedx, bird.speedz)
    screen.fill(black)
#    screen.blit(ball, ballrect)
    bird.update()
    screen.blit(bird.image, bird.rect)
    pygame.display.flip()
