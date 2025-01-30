from App.pieces.piece import Piece

DIAGONAL_DIRECTIONS = ("up_left", "up_right", "down_right", "down_left")


class Bishop(Piece):
    def __init__(self, is_white: bool):
        super().__init__("bishop", is_white)

    def get_possible_destinations(self, current_square):
        result = []
        for direction in DIAGONAL_DIRECTIONS:
            result += self.get_line_of_possible_squares(current_square, direction)
        return result
