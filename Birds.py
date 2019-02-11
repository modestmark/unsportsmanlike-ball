#!/bin/python3
# This module is for player-controlled bird objects

import pygame

class Bird(pygame.sprite.Sprite) :

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.imageFacing = dict()
        self.imageFacing['left'] = pygame.image.load("bird_small.png")
        self.imageFacing['right'] = pygame.transform.flip(self.imageFacing['left'], 1, 0)
        self.image = self.imageFacing['right']
        self.rect = self.image.get_rect()
        self.speedx = 0
        self.speedz = 0

    def control(self, x, z) :
        if (self.speedx < 7) and (x > 0) : 
            self.speedx += x
            self.image = self.imageFacing['right']
        elif (self.speedx > -7) and (x < 0) : 
            self.speedx += x
            self.image = self.imageFacing['left']
        if (self.speedz < 7) and (z > 0) : 
            self.speedz += z
        elif (self.speedz > -7) and (z < 0) : 
            self.speedz += z

    def update(self) :
        if self.speedz < 7 :
            self.speedz += 1

        self.rect = self.rect.move(self.speedx, self.speedz)

		
