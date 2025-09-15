import pygame

class Circle:

    def __init__(self, radius):
        self.circle_position = [960, 540]
        self.circle_radius = radius
        self.circle_color = (255, 255, 255)
        self.circle_width = 5  

    def draw(self, screen):
        pygame.draw.circle(
            screen,
            self.circle_color,
            self.circle_position,
            self.circle_radius,
            width=self.circle_width 
        )
