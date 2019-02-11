#!/bin/python3
# This module is for player-controlled bird objects

import pygame

class Bird(pygame.sprite.Sprite) :

    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bird_small.png")
        self.rect = self.image.get_rect()

    def control(self, x, z) :
        self.movex += x
        self.movez += z

    def update(self) :
        self.rect.x = self.rect.x + self.movex
        self.rect.z = self.rect.z + self.movez
		
