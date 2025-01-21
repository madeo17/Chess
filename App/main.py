import pygame

GREEN = (105, 130, 90)
WHITE = (245, 250, 210)
SQUARE_SIZE = 80

class Square(pygame.sprite.Sprite):

    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((SQUARE_SIZE, SQUARE_SIZE))
        self.color = WHITE
        self.surf.fill(self.color)
        self.rect = self.surf.get_rect()

    def draw(self, screen, x, y):
        screen.blit(self.surf, (x,y))

    def switch_color(self):
        if self.color == WHITE:
            self.color = GREEN
        else:
            self.color = WHITE
        self.surf.fill(self.color)


def draw_board(screen):
    square = Square()
    offset = SQUARE_SIZE
    def draw_rank(y):
        nonlocal screen, square, offset
        x = 50
        for _ in range(8):
            square.draw(screen, x, y)
            x += offset
            square.switch_color()
    y = 50
    for _ in range(8):
        draw_rank(y)
        y += offset
        square.switch_color()

pygame.init()
screen = pygame.display.set_mode((1200, 800))
draw_board(screen)
pygame.display.flip()

game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    # pygame.display.flip()

pygame.quit()
