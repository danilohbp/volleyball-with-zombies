#This was modified for soraprogrammer!
import pygame
import math

class Ball(pygame.sprite.Sprite):

    mais = 0

    def __init__(self, *groups):
        super().__init__(*groups)

        self.image = pygame.image.load("data/VolleyBall_ball32x32.png")
        self.image = pygame.transform.scale(self.image, [30, 30])
        self.rect = pygame.Rect(470, 50, 30, 30)
        self.rect = self.image.get_rect()
        self.speedx = 6
        self.speedy = 6
        

    def cross(self, crossTheCourt = False):
    	self.crossTheCourt = crossTheCourt
    	return self.crossTheCourt

    def update(self, *args):
        #self.timer += 0.03
        #self.rect.y = 220 + math.sin(self.timer) * 100

        self.rect.x += self.speedx
        self.rect.y += self.speedy 

        self.rect.move(self.speedx, self.speedy)
        
        if self.rect.top < 0 or self.rect.bottom > 480:
            self.speedy = -self.speedy
            
            #self.rect.y = self.speed

        if self.rect.left < 0 or self.rect.right > 840:
            self.speedx = -self.speedx  
            
            #self.rect.x = self.speed
            #self.kill()

        	#cross = False
        	#exist = self.cross(True)
        	#return cross, exist        

        #self.rect.x += self.speed[0]
        #self.rect.y += self.speed[1]

        #if self.rect.left < 0 or self.rect.right > 840:
        #    self.speed[0] = -self.speed[0]
        #if self.rect.top < 0 or self.rect.bottom > 480:
        #    self.speed[1] = -self.speed[1]
      




