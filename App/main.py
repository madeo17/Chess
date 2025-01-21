import pygame

class Square(pygame.sprite.Sprite):

    def __init__(self):
        super(Square, self).__init__()
        self.surf = pygame.Surface((25, 25))
        self.surf.fill((0, 200, 255))
        self.rect = self.surf.get_rect()


pygame.init()
screen = pygame.display.set_mode((1200, 800))

square = Square()


game_on = True
while game_on:

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_on = False

    screen.blit(square.surf, (50,50))

    pygame.display.flip()

pygame.quit()
