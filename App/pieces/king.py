from App.pieces.piece import Piece
from App.square import DIRECTIONS


class King(Piece):
    def __init__(self, is_white: bool):
        super().__init__("king", is_white)

    def get_possible_destinations(self, current_square):
        result = []
        for direction in DIRECTIONS:
            square = current_square(direction)
            if self.is_square_available(square):
                result.append(square)
        return result
