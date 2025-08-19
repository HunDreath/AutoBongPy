
import pygame as pygame
import sys as sys

pygame.init()

#Display settings

largeur = 1080
hauteur = 1920

screen = pygame.display.set_mode((largeur, hauteur));

backGroundColor = (0, 0, 0)
screen.fill(backGroundColor);

#Ball settings

ballColor = (255, 0, 0)
ballRadius = 40

backgroundBallColor = (255, 255, 255)
backgroundBallRadius = 45

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.draw.circle(screen, backgroundBallColor, [540,960], backgroundBallRadius)
    pygame.draw.circle(screen, ballColor, [540,960], ballRadius)
    
    pygame.display.flip()        

pygame.quit()
sys.exit()