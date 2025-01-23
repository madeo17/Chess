import pygame

SQUARE_SIZE = 80
GREEN = (105, 130, 90)
WHITE = (245, 250, 210)


class Square:
    def __init__(self, x : int, y : int, is_white : bool):
        self.rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = (x, y)
        self.is_white = is_white

    def draw(self, surface):
        color = WHITE if self.is_white else GREEN
        pygame.draw.rect(surface, color, self.rect)

    def switch_color(self):
        self.is_white = not self.is_white
