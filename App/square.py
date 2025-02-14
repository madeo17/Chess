import pygame

SQUARE_SIZE = 120
GREEN = (105, 130, 90)
WHITE = (245, 250, 210)
HIGHLIGHT_COLOR = (250, 250, 80)
ALL_DIRECTIONS = ("left", "up_left", "up", "up_right", "right", "down_right", "down", "down_left")
DIAGONAL_DIRECTIONS = ("up_left", "up_right", "down_right", "down_left")
STRAIGHT_DIRECTIONS = ("left", "up", "right", "down")


class Square:
    screen = None

    def __init__(self, x : int, y : int, is_white : bool):
        self.rect = pygame.Rect(0, 0, SQUARE_SIZE, SQUARE_SIZE)
        self.rect.center = (x, y)
        self.is_white = is_white
        self.neighbor = {direction: None for direction in ALL_DIRECTIONS}
        self.piece = None
        self.is_targeted = False
        self.action_on_move = None

        self.is_en_passant = False
        self.is_this_turn_en_passant = False

    def __call__(self, direction: str):
        return self.neighbor[direction]

    def draw(self):
        color = WHITE if self.is_white else GREEN
        pygame.draw.rect(Square.screen, color, self.rect)
        if self.is_targeted:
            pygame.draw.rect(Square.screen, HIGHLIGHT_COLOR, self.rect)
        if self.piece:
            self.piece.draw(Square.screen)

    def perform_additional_action_on_move(self):
        if self.action_on_move:
            self.action_on_move()
            self.action_on_move = None

    def put_piece(self, piece):
        self.piece = piece
        self.piece.set_center(self.rect.center)
        self.perform_additional_action_on_move()
        self.draw()

    def has_piece(self) -> bool:
        return self.piece is not None

    def switch_target_state(self, enable: bool, action=None):
        self.is_targeted = enable
        self.draw()
        if not enable:
            self.action_on_move = None
        elif action:
            self.action_on_move = action

    def move_piece(self, target_square):
        target_square.put_piece(self.piece)
        self.piece.moved = True
        self.piece = None
        self.draw()

    def remove_piece(self):
        self.piece = None
        self.draw()

    def mark_en_passant(self):
        self.is_en_passant = True
        self.is_this_turn_en_passant = True

    def update_en_passant_status(self):
        if self.is_en_passant:
            if self.is_this_turn_en_passant:
                self.is_this_turn_en_passant = False
            else:
                self.is_en_passant = False


def switch_squares_target_state(enable: bool, squares: list):
    for square in squares:
        square.switch_target_state(enable)

def update_en_passant_squares(squares: list):
    for square in squares:
        square.update_en_passant_status()
