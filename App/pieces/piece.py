import pygame
from pathlib import Path

IMAGE_SIZE = (226 * 0.24, 270 * 0.24)

class Piece:
    def __init__(self, name: str, is_white: bool):
        color = "white" if is_white else "black"
        image_path = Path('img', 'pieces', f'{color}_{name}.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        self.image = pygame.transform.scale(self.image, IMAGE_SIZE)
        self.rect = self.image.get_rect()
        self.is_white = is_white
        self.moved = False

    def get_image(self):
        return self.image

    def set_center(self, center):
        self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_same_side(self, piece):
        return self.is_white == piece.is_white

    def get_possible_destinations(self, current_square) -> list:
        return []
