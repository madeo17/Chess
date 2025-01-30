from App.pieces.piece import Piece
from App.square import DIRECTIONS


class Queen(Piece):
    def __init__(self, is_white: bool):
        super().__init__("queen", is_white)

    def get_possible_destinations(self, current_square):
        result = []
        for direction in DIRECTIONS:
            result += self.get_line_of_possible_squares(current_square, direction)
        return result
