import pygame
import sys
from generate.circle import Circle
from generate.balle import Balle  

def run_pygame():
    pygame.init()

    largeur = 1920
    hauteur = 1080
    screen = pygame.display.set_mode((largeur, hauteur))

    backGroundColor = (0, 0, 0)
    screen.fill(backGroundColor)

    ballColor = (255, 0, 0)
    backgroundBallColor = (255, 255, 255)

    ball = Balle(40, ballColor)
    backGroundBall = Balle(42, backgroundBallColor)

    running = True
    while running:

        backGroundBall.draw(screen)
        ball.draw(screen)

        circleRadius = 300
        for i in range(10):
            circle = Circle(circleRadius)
            circle.draw(screen)
            circleRadius += 20
            
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False    

        pygame.display.flip()

    pygame.quit()
    sys.exit()
