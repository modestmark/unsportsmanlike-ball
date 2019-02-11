#!/bin/python3
# This module is for player-controlled bird objects

import pygame

class Bird(pygame.sprite.Sprite) :

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bird_small.png")
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedz = 0

    def control(self, x, z) :
        if (self.speedx < 7) and (x > 0) : 
            self.speedx += x
        elif (self.speedx > -7) and (x < 0) : 
            self.speedx += x
        if (self.speedz < 7) and (z > 0) : 
            self.speedz += z
        elif (self.speedz > -7) and (z < 0) : 
            self.speedz += z

    def update(self) :
        if self.speedz < 7 :
            self.speedz += 1

        self.rect = self.rect.move(self.speedx, self.speedz)

		
