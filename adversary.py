import pygame
import math

class Adversary(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(470, 50, 100, 100)
        self.timer = 0
        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        self.timer += 0.03
        self.rect.y = 220 + math.sin(self.timer) * 100

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0
        elif self.rect.right > 840:
            self.rect.right = 840
            self.speed = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0


