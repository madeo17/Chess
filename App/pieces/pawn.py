from .piece import Piece


class Pawn(Piece):
    def __init__(self, is_white: bool):
        super().__init__("pawn", is_white)

    def get_possible_destinations(self, current_square):
        direction = "up" if self.is_white else "down"
        result = []

        if forward_square := current_square.neighbor[direction]:
            if not forward_square.has_piece():
                result.append(forward_square)
                if not self.moved:
                    if further_square := forward_square.neighbor[direction]:
                        if not further_square.has_piece():
                            result.append(further_square)
            for attack_direction in ("left", "right"):
                square = forward_square.neighbor[attack_direction]
                if square.has_piece() and not square.piece.is_same_side(self):
                    result.append(square)

        return result
