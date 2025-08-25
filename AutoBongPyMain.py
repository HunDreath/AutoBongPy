
import pygame as pygame
import sys as sys
from balle import Balle

pygame.init()

#Display settings

largeur = 1920
hauteur = 1080

screen = pygame.display.set_mode((largeur, hauteur));

backGroundColor = (0, 0, 0)
screen.fill(backGroundColor);

#Ball settings

ballColor = (255, 0, 0)
backgroundBallColor = (255, 255, 255)

ball = Balle(40, ballColor);
backGroundBall = Balle(42, backgroundBallColor);

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    ball.draw(screen);
    backGroundBall.draw(screen);
    
    pygame.display.flip()        

pygame.quit()
sys.exit()