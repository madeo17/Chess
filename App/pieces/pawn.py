from App.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, is_white: bool):
        super().__init__("pawn", is_white)

    def get_possible_destinations(self, current_square):
        direction = "up" if self.is_white else "down"
        result = []

        forward_square = current_square(direction)
        # no need to check if square exist because will never get to the edge (promotion)
        if not forward_square.has_piece():
            result.append(forward_square)
            if not self.moved:
                further_square = forward_square(direction)
                if further_square and not further_square.has_piece():
                    result.append(further_square)
        for attack_direction in ("left", "right"):
            square = forward_square(attack_direction)
            if square.has_piece() and not square.piece.is_same_side(self):
                result.append(square)

        return result
