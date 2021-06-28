import pygame
import math
import random

class Enemy(pygame.sprite.Sprite):

    __slots__ = ['image', 'rect', 'speed']

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/Jow_ETE.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 20)
        self.rect.x = 0
        self.rect.y = random.randint(1, 400)
        self.speed = 1 + random.random() * 2

    def update(self, *args):
        #self.timer += 0.03
        #self.rect.x = 100 + math.sin(self.timer) * 100
        self.rect.x += self.speed
        if self.rect.right > 870:
            self.kill()
            



