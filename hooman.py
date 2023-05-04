import pygame

import config


class Hooman:
    def __init__(self, x, y):
        self.position = [x, y]
        self.width = 10
        self.height = 10
        self.rect = pygame.Rect(self.position[0] * 10, self.position[1] * 10, self.width, self.height)

    def draw(self, screen):
        pygame.draw.rect(screen, (255, 255, 255), self.rect)

    def update(self, dx, dy):
        new_x = self.position[0] + dx
        new_y = self.position[1] + dy

        if 0 <= new_x < config.screen_width / 10 and 0 <= new_y < config.screen_height / 10:
            self.position = [new_x, new_y]
            self.rect.topleft = [new_x * 10, new_y * 10]