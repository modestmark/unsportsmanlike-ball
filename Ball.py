import pygame

class Bird(pygame.sprite.Sprite) :
    def __init__(self) :
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load("ball.png")
self.rect = self.image.get_rect()