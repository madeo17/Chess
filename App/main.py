import pygame

from chessboard import Chessboard

pygame.init()
screen = pygame.display.set_mode((1200, 800))
pygame.display.set_caption("Chess")

chessboard = Chessboard(screen)
chessboard.draw()

chessboard.init_all_pieces()

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
