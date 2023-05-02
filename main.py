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

screen = pygame.display.set_mode((1000, 1000))

square = WhiteSquare(50, 50, 10, 10)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        square.update(0, -10)
    if keys[pygame.K_DOWN]:
        square.update(0, 10)
    if keys[pygame.K_LEFT]:
        square.update(-10, 0)
    if keys[pygame.K_RIGHT]:
        square.update(10, 0)

    screen.fill((0, 0, 0))
    for i in range(0, 1000, 10):
        for j in range(0, 1000, 10):
            pygame.draw.rect(screen, (0, 0, 0), pygame.Rect(i, j, 10, 10), 1)
    square.draw(screen)
    pygame.display.flip()

    pygame.time.Clock().tick(60)