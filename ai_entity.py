import random
import pygame
from hooman import Hooman

class AIEntity(Hooman):
    def __init__(self, x, y, color):
        super().__init__(x, y)
        self.color = color
        self.life = 500
        self.reward_threshold = 100
        self.moves_since_last_reproduction = 0

    def draw(self, screen):
        pygame.draw.rect(screen, self.color, self.rect)

    def ai_move(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dx, dy = random.choice(directions)
        self.update(dx, dy)
        self.life -= 1

    def update_reward(self, reward):
        self.reward += reward

    def is_dead(self):
        return self.life <= 0

    def is_eligible_for_reproduction(self, other_entities):
        if self.moves_since_last_reproduction >= 100 and self.life >= 200:
            for other in other_entities:
                if other == self:
                    continue

                dx = abs(self.position[0] - other.position[0])
                dy = abs(self.position[1] - other.position[1])
                distance = max(dx, dy)

                if distance <= 5:
                    return other
        return None

    def pass_parameters(self):
        return {
            "color": self.color,
            "max_life": self.max_life,
            "reward_threshold": self.reward_threshold,
        }

    def ai_move(self):
        directions = [(0, -1), (0, 1), (-1, 0), (1, 0)]
        dx, dy = random.choice(directions)
        self.update(dx, dy)
        self.life -= 1
        self.moves_since_last_reproduction += 1

    def is_close_to_same_color_entity(self, other_entities):
        for other in other_entities:
            if other.color == self.color:
                dx = abs(self.position[0] - other.position[0])
                dy = abs(self.position[1] - other.position[1])
                distance = max(dx, dy)

                if distance <= 5:
                    return True
        return False

    def is_younger_than(self, other):
        return self.life > other.life