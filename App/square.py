import pygame

SQUARE_SIZE = 80
GREEN = (105, 130, 90)
WHITE = (245, 250, 210)
HIGHLIGHT_COLOR = (250, 250, 80)


class Square:
    screen = None

    def __init__(self, x : int, y : int, is_white : bool):
        self.rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = (x, y)
        self.is_white = is_white
        self.neighbor = {"left": None, "up": None, "right": None, "down": None}
        self.piece = None
        self.highlight = False

    def draw(self):
        color = WHITE if self.is_white else GREEN
        pygame.draw.rect(Square.screen, color, self.rect)
        if self.highlight:
            pygame.draw.rect(Square.screen, HIGHLIGHT_COLOR, self.rect)
        if self.piece:
            self.piece.draw(Square.screen)
            # Square.screen.blit(self.piece.get_image(), self.rect.center)

    def switch_color(self):
        self.is_white = not self.is_white

    def put_piece(self, piece):
        self.piece = piece
        self.piece.set_center(self.rect.center)
        self.draw()

    def has_piece(self) -> bool:
        return self.piece is not None

    def switch_highlight(self, enable: bool):
        self.highlight = enable
        self.draw()

    def is_highlighted(self) -> bool:
        return self.highlight

    def get_possible_destinations(self):
        if self.piece:
            return self.piece.get_possible_destinations(self)
        return None

    def move_piece(self, target_square):
        target_square.put_piece(self.piece)
        self.piece.moved = True
        self.piece = None
        self.draw()
