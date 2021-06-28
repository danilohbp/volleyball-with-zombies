import pygame
import random
from player import Player
from adversary import Adversary
from enemy import Enemy
from ball import Ball

class Game:
    pygame.init()
    SCREEN_WIDTH = 840
    SCREEN_HEIGHT = 480
    size = [SCREEN_WIDTH, SCREEN_HEIGHT]
    bigfont = pygame.font.Font(None, 80)
    display = pygame.display.set_mode(size)
    pygame.display.set_caption("Volleyball with Zombies")


    # Objects
    objectGroup = pygame.sprite.Group()
    ballGroup = pygame.sprite.Group()
    obstacleGroup = pygame.sprite.Group()


    # Background
    bg = pygame.sprite.Sprite(objectGroup)
    bg.image = pygame.image.load("data/volleyBall_court_840x480.png")
    bg.image = pygame.transform.scale(bg.image, size)
    bg.rect = bg.image.get_rect()

    player1 = Player(objectGroup)
    player2 = Adversary(objectGroup)

    # Music
    pygame.mixer.music.load("data/awesomeness.wav")
    pygame.mixer.music.play(-1)


    # Sounds
    shoot = pygame.mixer.Sound("data/shooting.ogg")


    # Ball Logic
    speed = [10, 10]
    ball = pygame.image.load("data/VolleyBall_ball32x32.png")
    ballrect = ball.get_rect()
            

    gameLoop = True
    gameOver = False
    timer = 0
    clock = pygame.time.Clock()
    exist = False
    cross = False
    obstacle = None
    if __name__ == "__main__":
        while gameLoop:
            clock.tick(60)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    gameLoop = False

                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_k:
                        if exist == False and cross == False:
                            ball = Ball(objectGroup, ballGroup)
                            ball.rect.center = player1.rect.center
                            ball.rect.x += 10
                            ball.rect.y += 10
                            shoot.play()
                        exist = True
                        
                        
                    if event.key == pygame.K_SPACE:
                        gameOver = False


            if not gameOver:

                #Update and Logic

                objectGroup.update()

                collisionBetweenObstacleBall = 0
                

                timer += 1
                if timer > 30:
                    timer = 0
                    if random.random() < 0.1:
                        obstacles = Enemy(objectGroup, obstacleGroup)
                        obstacle = True
                        


                collisionBetweenObstacle = pygame.sprite.spritecollide(player1, obstacleGroup, True, pygame.sprite.collide_mask)
                collisionBetweenPlayer1Ball = pygame.sprite.spritecollide(player1, ballGroup, False, pygame.sprite.collide_mask)
                collisionBetweenPlayer2Ball = pygame.sprite.spritecollide(player2, ballGroup, False, pygame.sprite.collide_mask)
                

                if collisionBetweenObstacle:
                    print("Game Over!")
                    gameOver = True
                    if ball:
                        print('ok')
                    exist = False

                if collisionBetweenPlayer1Ball:
                    keys = pygame.key.get_pressed()
                    if  keys[pygame.K_w] or keys[pygame.K_s]: 
                        ball.speedx = -ball.speedx
                        ball.speedy = -ball.speedy

                    else:
                        ball.speedx = -ball.speedx
                        ball.speedy = -ball.speedy
                        
                    #ball.speed = -ball.speed

                if collisionBetweenPlayer2Ball:
                    ball.speedx = -ball.speedx
                    ball.speedy = -ball.speedy

                if obstacle == True:
                    collisionBetweenObstacleBall = pygame.sprite.spritecollide(obstacles, ballGroup, False, pygame.sprite.collide_mask)
                    if collisionBetweenObstacleBall:
                        ball.speedx = -ball.speedx
                        ball.speedy = -ball.speedy

            # Draw
            display.fill([19, 173, 235])
            objectGroup.draw(display)
            
            if gameOver == True:
                text = bigfont.render('Play again?', 24, (0, 0, 0))
                textx = SCREEN_WIDTH / 2 - text.get_width() / 2
                texty = SCREEN_HEIGHT / 2 - text.get_height() / 2
                textx_size = text.get_width()
                texty_size = text.get_height()
                pygame.draw.rect(display, [255, 255, 255, 255], ((textx - 5, texty - 5),(textx_size + 10, texty_size+10)))
                display.blit(text, (SCREEN_WIDTH / 2 - text.get_width() / 2, SCREEN_HEIGHT / 2 - text.get_height() / 2))
            pygame.display.update()

Game()

