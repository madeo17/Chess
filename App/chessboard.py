from square import Square, SQUARE_SIZE
from utils import switch_highlight_on_squares
from pieces.pawn import Pawn
from pieces.bishop import Bishop
from pieces.knight import Knight
from pieces.rook import Rook
from pieces.queen import Queen
from pieces.king import King


INITIAL_COORD = 100
SQUARES_RANGE = range(8)
WHITE_PAWNS_RANK_IDX = 6
BLACK_PAWNS_RANK_IDX = 1
WHITE_NON_PAWNS_RANK_IDX = 7
BLACK_NON_PAWNS_RANK_IDX = 0


class Chessboard:
    def __init__(self, screen):
        self.board = []
        self.screen = Square.screen = screen
        self.__init_board()
        self.__init_squares_neighbors()
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

    def __init_squares_neighbors(self):
        for i, rank in enumerate(self.board):
            for j, square in enumerate(rank):
                if j - 1 in SQUARES_RANGE:
                    square.neighbor["left"] = rank[j - 1]
                    if i - 1 in SQUARES_RANGE:
                        square.neighbor["up_left"] = self.board[i - 1][j - 1]
                    if i + 1 in SQUARES_RANGE:
                        square.neighbor["down_left"] = self.board[i + 1][j - 1]
                if j + 1 in SQUARES_RANGE:
                    square.neighbor["right"] = rank[j + 1]
                    if i - 1 in SQUARES_RANGE:
                        square.neighbor["up_right"] = self.board[i - 1][j + 1]
                    if i + 1 in SQUARES_RANGE:
                        square.neighbor["down_right"] = self.board[i + 1][j + 1]
                if i - 1 in SQUARES_RANGE:
                    square.neighbor["up"] = self.board[i - 1][j]
                if i + 1 in SQUARES_RANGE:
                    square.neighbor["down"] = self.board[i + 1][j]

    def draw(self):
        for rank in self.board:
            for square in rank:
                square.draw()

    def init_pawns(self, is_white: bool):
        rank_idx = WHITE_PAWNS_RANK_IDX if is_white else BLACK_PAWNS_RANK_IDX
        for square in self.board[rank_idx]:
            square.put_piece(Pawn(is_white))

    def init_major_minor_pieces(self, is_white:bool):
        rank_idx = WHITE_NON_PAWNS_RANK_IDX if is_white else BLACK_NON_PAWNS_RANK_IDX
        for i, piece in enumerate((Rook, Knight, Bishop, Queen, King, Bishop, Knight, Rook)):
            self.board[rank_idx][i].put_piece(piece(is_white))

    def init_all_pieces(self):
        for is_white in (True, False):
            self.init_pawns(is_white)
            self.init_major_minor_pieces(is_white)

    def get_clicked_square(self, x, y):
        for rank in self.board:
            for square in rank:
                if square.rect.collidepoint(x, y):
                    return square
        return None

    def turn_off_highlight_on_all_squares(self):
        for rank in self.board:
            switch_highlight_on_squares(enable=False, squares=rank)

    def move_ready_piece(self, target_square):
        self.square_with_piece_ready_to_move.move_piece(target_square)
        self.square_with_piece_ready_to_move = None
        self.turn_off_highlight_on_all_squares()

    def handle_click(self, x, y):
        if not (square := self.get_clicked_square(x, y)):
            return
        if self.square_with_piece_ready_to_move and square.is_highlighted():
            self.move_ready_piece(square)
        elif square.has_piece():
            self.turn_off_highlight_on_all_squares()
            possible_destinations = square.get_possible_destinations()
            if possible_destinations:
                switch_highlight_on_squares(enable=True, squares=possible_destinations)
                self.square_with_piece_ready_to_move = square
        else:
            self.turn_off_highlight_on_all_squares()
