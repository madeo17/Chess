from square import Square, SQUARE_SIZE

INITIAL_COORD = 100
SQUARES_IN_RANK = 8


class Chessboard:
    def __init__(self):
        self.board = []
        self.init_board()

    def init_board(self):
        is_white = True
        shift = SQUARE_SIZE
        y = INITIAL_COORD
        for _ in range(SQUARES_IN_RANK):
            rank = []
            x = INITIAL_COORD
            for _ in range(SQUARES_IN_RANK):
                square = Square(x, y, is_white)
                x += shift
                is_white = not is_white
                rank.append(square)
            self.board.append(rank)
            is_white = not is_white
            y += shift

    def draw(self, screen):
        for rank in self.board:
            for square in rank:
                square.draw(screen)
