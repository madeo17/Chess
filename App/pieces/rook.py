from App.pieces.piece import Piece

STRAIGHT_DIRECTIONS = ("left", "up", "right", "down")


class Rook(Piece):
    def __init__(self, is_white: bool):
        super().__init__("rook", is_white)

    def get_possible_destinations(self, current_square):
        result = []
        for direction in STRAIGHT_DIRECTIONS:
            result += self.get_line_of_possible_squares(current_square, direction)
        return result
