
import pygame


class Player(pygame.sprite.Sprite):
    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/player.png")
        self.image = pygame.transform.scale(self.image, [100, 100])
        self.rect = pygame.Rect(50, 50, 100, 100)

        self.speed = 0
        self.acceleration = 0.1

    def update(self, *args):
        # Lógica do jogo
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            #self.speed -= self.acceleration
            self.rect.x -= 10
        elif keys[pygame.K_d]:
            #self.speed += self.acceleration
            self.rect.x += 10
        elif keys[pygame.K_w]:
            self.rect.y -= 10
        elif keys[pygame.K_s]:
            self.rect.y += 10
        #else:
            #self.speed *= 0.95

        #self.rect.x += self.speed

        if self.rect.top < 0:
            self.rect.top = 0
            self.speed = 0
        elif self.rect.bottom > 480:
            self.rect.bottom = 480
            self.speed = 0
        elif self.rect.right > 440:
            self.rect.right = 440
            self.speed = 0
        elif self.rect.left < 0:
            self.rect.left = 0
            self.speed = 0


