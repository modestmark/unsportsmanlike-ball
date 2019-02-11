#!/bin/python3
# This module is for player-controlled bird objects

import pygame

class Bird(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("bird.jpg")
        self.rect = self.image.get_rect()
		
