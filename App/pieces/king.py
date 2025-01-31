from App.pieces.piece import Piece
from App.square import ALL_DIRECTIONS
from App.pieces.rook import Rook


class King(Piece):
    def __init__(self, is_white: bool):
        super().__init__("king", is_white)

    def get_castle_destinations(self, current_square):
        result = []
        if not self.moved:
            for direction in ("left", "right"):
                neighbor_square = current_square(direction)
                if not neighbor_square.has_piece():
                    second_square = neighbor_square(direction)
                    if not second_square.has_piece():
                        third_square = second_square(direction)
                        if direction == "right":
                            if check_for_rook(third_square):
                                result.append((second_square, third_square))
                        elif not third_square.has_piece():
                            fourth_square = third_square(direction)
                            if check_for_rook(fourth_square):
                                result.append((second_square,fourth_square))
        return result

    def target_squares(self, current_square) -> bool:
        is_any_targeted = False

        for direction in ALL_DIRECTIONS:
            square = current_square(direction)
            if self.is_square_available(square):
                square.switch_target_state(True)
                is_any_targeted = True

        for king_target_square, rook_square in self.get_castle_destinations(current_square):
            king_target_square.switch_target_state(True, action=get_castle_action(rook_square))
            is_any_targeted = True

        return is_any_targeted


def check_for_rook(square) -> bool:
    return square.has_piece() and isinstance(square.piece, Rook) and not square.piece.moved

def get_castle_action(rook_square):
    def castle_action():
        if rook_square("left"):
            target_square = rook_square("left")("left")
        else:
            target_square = rook_square("right")("right")("right")
        rook_square.move_piece(target_square)
    return castle_action
