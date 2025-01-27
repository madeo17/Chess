import pygame

IMAGE_SIZE = (226 * 0.24, 270 * 0.24)

class Bishop:
    def __init__(self):
        self.image = pygame.image.load('img\\pieces\\bishop.png').convert_alpha()
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.is_white = True

    def get_image(self):
        return self.image

    def set_center(self, center):
        self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_same_side(self, is_white):
        return self.is_white == is_white

    def get_possible_dest(self, current_square):
        return current_square.get_upper_left_diagonal(self.is_white)
