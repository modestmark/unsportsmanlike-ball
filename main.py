#!/bin/python3
#This is the initial framework code for a sportsball like game

import sys, pygame
from Birds import Bird
from Ball import Ball




pygame.init()

clockobject = pygame.time.Clock()
keys=pygame.key.get_pressed()

size = width, height = 1080, 720



screen = pygame.display.set_mode(size)

background_image = pygame.image.load("Background1.png")
screen.blit(background_image, [0, 0])

bird = Bird()
ball = Ball()

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

    if bird.hitbox.left < 0:
        bird.speedx = +2
    if bird.hitbox.right > width:
        bird.speedx = -2
    if bird.hitbox.top < 0:
        bird.speedz = +2
    if (bird.hitbox.bottom > height) and (bird.speedz > 0):
        bird.speedz = -2

    if ball.rect.left < 0:
        ball.speedx = -(ball.speedx + 3)
    if ball.rect.right > width:
        ball.speedx = -(ball.speedx + 3)
    if ball.rect.top < 0:
        ball.speedz = -(ball.speedz + 3)
    if ball.rect.bottom > height:
        ball.speedz = -(ball.speedz + 3)


    if ball.rect.colliderect(bird.hitbox) == 1:
        ball.contact(bird.rect.centerx, bird.rect.centery, ball.rect.centerx, ball.rect.centery)

   # print(bird.speedx, bird.speedz)
    screen.blit(background_image, [0, 0])

    bird.update()
    ball.update()
    screen.blit(bird.image, bird.rect)
    screen.blit(ball.image, ball.rect)
    pygame.display.flip()
