from App.pieces.piece import Piece

STRAIGHT_DIRECTIONS = ("left", "up", "right", "down")


class Rook(Piece):
    def __init__(self, is_white: bool):
        super().__init__("rook", is_white)

    def target_squares(self, current_square) -> bool:
        is_any_targeted = False
        for direction in STRAIGHT_DIRECTIONS:
            for square in self.get_line_of_possible_squares(current_square, direction):
                square.switch_target_state(True)
                is_any_targeted = True
        return is_any_targeted
