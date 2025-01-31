from App.pieces.piece import Piece


class Pawn(Piece):
    def __init__(self, is_white: bool):
        super().__init__("pawn", is_white)

    def target_squares(self, current_square) -> bool:
        direction = "up" if self.is_white else "down"
        is_any_targeted = False

        forward_square = current_square(direction)
        # no need to check if square exist because will never get to the edge (promotion)
        if not forward_square.has_piece():
            forward_square.switch_target_state(True)
            is_any_targeted = True
            if not self.moved:
                further_square = forward_square(direction)
                if further_square and not further_square.has_piece():
                    further_square.switch_target_state(True)
                    is_any_targeted = True
        for attack_direction in ("left", "right"):
            square = forward_square(attack_direction)
            if square and square.has_piece() and not square.piece.is_same_side(self):
                square.switch_target_state(True)
                is_any_targeted = True

        return is_any_targeted
