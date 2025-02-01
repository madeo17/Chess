from App.pieces.piece import Piece


class Knight(Piece):
    def __init__(self, is_white: bool):
        super().__init__("knight", is_white)

    def target_squares(self, current_square) -> bool:
        is_any_targeted = False

        for direction in ("left", "right"):
            if square := current_square(direction):
                if second_square := square(direction):
                    for turn in ("up", "down"):
                        destination_square = second_square(turn)
                        if self.is_square_accessible(destination_square):
                            destination_square.switch_target_state(True)
                            is_any_targeted = True

        for direction in ("up", "down"):
            if square := current_square(direction):
                if second_square := square(direction):
                    for turn in ("left", "right"):
                        destination_square = second_square(turn)
                        if self.is_square_accessible(destination_square):
                            destination_square.switch_target_state(True)
                            is_any_targeted = True

        return is_any_targeted
