import pygame

class Ball(pygame.sprite.Sprite) :

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Ball1.png')
        self.rect = self.image.get_rect()
        self.speedx = 4
        self.speedz = 4

    def update(self) :
        if self.speedz < 7:
            self.speedz += 1



        self.rect = self.rect.move(self.speedx, self.speedz)


    def contact(self, rect, vector):
        (angle,z) = vector
        (dx,dy) = (z*math.cos(angle),z*math.sin(angle))
        return rect.move(dx,dy)