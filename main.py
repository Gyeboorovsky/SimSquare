import pygame
import sys

class WhiteSquare:
    def __init__(self, x, y, width, height):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def update(self, dx, dy):
        self.x += dx
        self.y += dy
        self.rect = pygame.Rect(self.x, self.y, self.width, self.height)

pygame.init()

screen = pygame.display.set_mode((100, 100))

square = WhiteSquare(50, 50, 10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.update(0, -1)
    if keys[pygame.K_DOWN]:
        square.update(0, 1)
    if keys[pygame.K_LEFT]:
        square.update(-1, 0)
    if keys[pygame.K_RIGHT]:
        square.update(1, 0)

    screen.fill((0, 0, 0))
    square.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)