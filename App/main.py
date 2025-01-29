import pygame
from chessboard import Chessboard
from pieces.bishop import Bishop
from pieces.pawn import Pawn
from pieces.rook import Rook


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chess")

chessboard = Chessboard(screen)
chessboard.draw()

# initialize some pieces for testing
chessboard.board[4][4].put_piece(Bishop(True))
chessboard.board[1][3].put_piece(Pawn(False))
chessboard.board[6][6].put_piece(Rook(True))

pygame.display.flip()

game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            x, y = pygame.mouse.get_pos()
            chessboard.handle_click(x, y)

            pygame.display.flip()

pygame.quit()
