import pygame

class Ball(pygame.sprite.Sprite) :

    def __init__(self):
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.image.load('Ball1.png')
        self.rect = self.image.get_rect()
        self.speedx = 2
        self.speedz = 2
        self.rect = self.rect.move(200, 200)

    def update(self) :
        if self.speedz < 7:
            self.speedz += 1



        self.rect = self.rect.move(self.speedx, self.speedz)


    def contact(self, birdx, birdz, ballx, ballz):
            speed = 1

            pushx = (ballx - birdx)
            pushz = (ballz - birdz)

            self.speedx = pushx + speed
            self.speedz = pushz + speed

