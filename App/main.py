import pygame
from chessboard import Chessboard
from bishop import Bishop


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chess")

chessboard = Chessboard(screen)
chessboard.draw()

# initialize one bishop for testing
chessboard.board[4][4].put_piece(Bishop())

pygame.display.flip()

game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # pygame.display.flip()

pygame.quit()
