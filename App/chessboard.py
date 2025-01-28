from square import Square, SQUARE_SIZE
from utils import switch_highlight_on_squares

INITIAL_COORD = 100
SQUARES_RANGE = range(8)


class Chessboard:
    def __init__(self, screen):
        self.board = []
        self.screen = Square.screen = screen
        self.__init_board()
        self.__init_connections_between_squares()
        self.square_with_piece_ready_to_move = None

    def __init_board(self):
        is_white = True
        shift = SQUARE_SIZE
        y = INITIAL_COORD
        for _ in SQUARES_RANGE:
            rank = []
            x = INITIAL_COORD
            for _ in SQUARES_RANGE:
                square = Square(x, y, is_white)
                rank.append(square)
                x += shift
                is_white = not is_white
            self.board.append(rank)
            is_white = not is_white
            y += shift

    def __init_connections_between_squares(self):
        for i, rank in enumerate(self.board):
            for j, square in enumerate(rank):
                square.left = rank[j - 1] if j - 1 in SQUARES_RANGE else None
                square.right = rank[j + 1] if j + 1 in SQUARES_RANGE else None
                square.up = self.board[i - 1][j] if i - 1 in SQUARES_RANGE else None
                square.down = self.board[i + 1][j] if i + 1 in SQUARES_RANGE else None

    def draw(self):
        for rank in self.board:
            for square in rank:
                square.draw()

    def get_clicked_square(self, x, y):
        for rank in self.board:
            for square in rank:
                if square.rect.collidepoint(x, y):
                    return square
        return None

    def turn_off_highlight_on_all_squares(self):
        for rank in self.board:
            switch_highlight_on_squares(enable=False, squares=rank)


    def handle_click(self, x, y):
        square = self.get_clicked_square(x, y)
        if self.square_with_piece_ready_to_move and square.is_highlighted():
            self.square_with_piece_ready_to_move.move_piece(square)
            self.square_with_piece_ready_to_move = None
            self.turn_off_highlight_on_all_squares()
        elif square.has_piece():
            possible_destinations = square.get_possible_destinations()
            if possible_destinations:
                switch_highlight_on_squares(enable=True, squares=possible_destinations)
                self.square_with_piece_ready_to_move = square
        else:
            self.turn_off_highlight_on_all_squares()
