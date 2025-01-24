from square import Square, SQUARE_SIZE

INITIAL_COORD = 100
SQUARES_RANGE = range(8)


class Chessboard:
    def __init__(self):
        self.board = []
        self.__init_board()
        self.__init_connections_between_squares()

    def draw(self, screen):
        for rank in self.board:
            for square in rank:
                square.draw(screen)

    def __init_board(self):
        is_white = True
        shift = SQUARE_SIZE
        y = INITIAL_COORD
        for _ in SQUARES_RANGE:
            rank = []
            x = INITIAL_COORD
            for _ in SQUARES_RANGE:
                square = Square(x, y, is_white)
                x += shift
                is_white = not is_white
                rank.append(square)
            self.board.append(rank)
            is_white = not is_white
            y += shift

    def __init_connections_between_squares(self):
        for i, rank in enumerate(self.board):
            for j, square in enumerate(rank):
                square.left = rank[j - 1] if j - 1 in SQUARES_RANGE else None
                square.right = rank[j + 1] if j + 1 in SQUARES_RANGE else None
                square.up = self.board[i - 1][i] if i - 1 in SQUARES_RANGE else None
                square.down = self.board[i + 1][i] if i + 1 in SQUARES_RANGE else None
