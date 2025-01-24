import pygame
from chessboard import Chessboard


pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chess")

chessboard = Chessboard()
chessboard.draw(screen)
pygame.display.flip()

game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # pygame.display.flip()

pygame.quit()
