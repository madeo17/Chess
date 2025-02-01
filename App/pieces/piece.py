import pygame
from pathlib import Path
from App.square import SQUARE_SIZE

IMAGE_SIZE = (226 * 0.24, 270 * 0.24)

class Piece:
    def __init__(self, name: str, is_white: bool):
        self.is_white = is_white
        self.__init_image(name)
        self.rect = self.image.get_rect()
        self.moved = False

    def __init_image(self, name):
        color = "white" if self.is_white else "black"
        image_path = Path('img', 'pieces', f'{color}_{name}.png')
        self.image = pygame.image.load(image_path).convert_alpha()
        original_width, original_height = self.image.get_size()
        aspect_ratio = original_width / original_height
        new_width = SQUARE_SIZE
        new_height = int(SQUARE_SIZE / aspect_ratio)
        self.image = pygame.transform.smoothscale(self.image, (new_width, new_height))

    def get_image(self):
        return self.image

    def set_center(self, center):
        self.rect.center = center

    def draw(self, surface):
        surface.blit(self.image, self.rect.topleft)

    def is_same_side(self, piece):
        return self.is_white == piece.is_white

    def is_square_accessible(self, square) -> bool:
        """
        Check if square is empty or with opponent piece.
        """
        if not square:
            return False
        if square.has_piece():
            return not square.piece.is_same_side(self)
        return True

    def get_line_of_possible_squares(self, square, direction: str) -> list:
        """
        Get line of squares on a given direction with possible destinations.
        """
        next_square = square(direction)
        if self.is_square_accessible(next_square):
            if next_square.has_piece():
                return [next_square]
            return [next_square] + self.get_line_of_possible_squares(next_square, direction)
        return []

    def target_squares(self, current_square) -> bool:
        """
        Implemented by concrete pieces.
        """
        pass
