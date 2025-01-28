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

    def get_diagonal(self, square, horizontal: str, vertical: str) -> list:
        """
        Get diagonal with possible destinations
        :param square: starting square
        :param horizontal: left or right
        :param vertical: up or down
        :return: list of squares
        """
        if square.neighbor[horizontal] and (next_square := square.neighbor[horizontal].neighbor[vertical]):
            if not next_square.has_piece():
                return [next_square] + self.get_diagonal(next_square, horizontal, vertical)
            else:
                if next_square.piece.is_same_side(self.is_white):
                    return []
                else:
                    return [next_square]
        else:
            return []

    def get_possible_destinations(self, current_square):
        result = []
        for horizontal in ("left", "right"):
            for vertical in ("up", "down"):
                result += self.get_diagonal(current_square, horizontal, vertical)
        return result
