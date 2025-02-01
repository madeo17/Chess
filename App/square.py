import pygame

SQUARE_SIZE = 120
GREEN = (105, 130, 90)
WHITE = (245, 250, 210)
HIGHLIGHT_COLOR = (250, 250, 80)
ALL_DIRECTIONS = ("left", "up_left", "up", "up_right", "right", "down_right", "down", "down_left")


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

    def __call__(self, direction: str):
        return self.neighbor[direction]

    def draw(self):
        color = WHITE if self.is_white else GREEN
        pygame.draw.rect(Square.screen, color, self.rect)
        if self.is_targeted:
            pygame.draw.rect(Square.screen, HIGHLIGHT_COLOR, self.rect)
        if self.piece:
            self.piece.draw(Square.screen)

    def switch_color(self):
        self.is_white = not self.is_white

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
