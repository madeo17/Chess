import pygame

SQUARE_SIZE = 80
GREEN = (105, 130, 90)
WHITE = (245, 250, 210)


class Square:
    screen = None

    def __init__(self, x : int, y : int, is_white : bool):
        self.rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = (x, y)
        self.is_white = is_white
        self.left = None
        self.right = None
        self.up = None
        self.down = None
        self.piece = None

    def draw(self):
        color = WHITE if self.is_white else GREEN
        pygame.draw.rect(Square.screen, color, self.rect)
        if self.piece:
            self.piece.draw(Square.screen)
            # Square.screen.blit(self.piece.get_image(), self.rect.center)

    def switch_color(self):
        self.is_white = not self.is_white

    def put_piece(self, piece):
        self.piece = piece
        self.piece.set_center(self.rect.center)
        self.draw()

    def get_upper_left_diagonal(self, is_piece_white) -> list:
        if self.left and (next_square := self.left.up):
            if not next_square.piece:
                return [next_square] + next_square.get_upper_left_diagonal()
            else:
                if next_square.piece.is_same_side(is_piece_white):
                    return []
                else:
                    return [next_square]
        else:
            return []
