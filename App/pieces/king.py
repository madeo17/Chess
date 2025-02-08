from App.pieces.knight import Knight
from App.pieces.piece import Piece
from App.pieces.rook import Rook
from App.pieces.bishop import Bishop
from App.pieces.queen import Queen
from App.pieces.pawn import Pawn
from App.square import ALL_DIRECTIONS, STRAIGHT_DIRECTIONS, DIAGONAL_DIRECTIONS


class King(Piece):
    def __init__(self, is_white: bool):
        super().__init__("king", is_white)

    def get_castle_destinations(self, current_square):
        result = []
        if not self.moved:
            for direction in ("left", "right"):
                neighbor_square = current_square(direction)
                if not neighbor_square.has_piece() and not is_square_threatened(neighbor_square, self):
                    second_square = neighbor_square(direction)
                    if not second_square.has_piece() and not is_square_threatened(second_square, self):
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
            if self.is_square_accessible(square) and not is_square_threatened(square, self):
                square.switch_target_state(True)
                is_any_targeted = True

        for king_target_square, rook_square in self.get_castle_destinations(current_square):
            king_target_square.switch_target_state(True, action=get_castle_action(rook_square))
            is_any_targeted = True

        return is_any_targeted


def is_square_threatened(square, king):
    """
    Check if square is attacked for a potential move of a given king.
    The trick is to find also the attackers that have the king on its way.
    """
    attackers = get_king_attackers(square, king, ALL_DIRECTIONS)
    pawn_directions = ("up_left", "up_right") if king.is_white else ("down_right", "down_left")

    for piece, direction, is_close in attackers:
        if (isinstance(piece, Queen)
                or (isinstance(piece, Bishop) and direction in DIAGONAL_DIRECTIONS)
                or (isinstance(piece, Rook) and direction in STRAIGHT_DIRECTIONS)
                or (isinstance(piece, King) and is_close)
                or (isinstance(piece, Pawn) and is_close and direction in pawn_directions)):
            return True
    return is_square_threatened_by_knight(square, king)

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

def get_directional_attacker_of_king(square, direction: str, king) -> tuple:
    """
    Get all potential attackers of king from a given direction for a square
    that the king is planning to go to.
    """
    is_close = True
    while square := square(direction):
        if square.has_piece() and square.piece is not king:
            piece = square.piece
            if not piece.is_same_side(king):
                return piece, direction, is_close
            return ()
        else:
            is_close = False
    return ()

def is_square_threatened_by_knight(square, king):
    for direction in ("left", "right"):
        if neighbor_square := square(direction):
            if second_square := neighbor_square(direction):
                for turn in ("up", "down"):
                    if knight_square := second_square(turn):
                        if piece := knight_square.piece:
                            if isinstance(piece, Knight) and not piece.is_same_side(king):
                                return True
    for direction in ("up", "down"):
        if neighbor_square := square(direction):
            if second_square := neighbor_square(direction):
                for turn in ("left", "right"):
                    if knight_square := second_square(turn):
                        if piece := knight_square.piece:
                            if isinstance(piece, Knight) and not piece.is_same_side(king):
                                return True

def get_king_attackers(square, king, directions):
    result = []
    for direction in directions:
        if attacker := get_directional_attacker_of_king(square, direction, king):
            result.append(attacker)
    return result
