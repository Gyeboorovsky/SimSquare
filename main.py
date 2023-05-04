import pygame
import sys

import config
from entity_generator import EntityGenerator
from hooman import Hooman
from ai_entity import AIEntity

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((config.screen_width, config.screen_height))
        self.hooman = Hooman(5, 5)

        self.ai_entities = EntityGenerator.initial_state(self)
        self.entity_generator = EntityGenerator()
        self.clock = pygame.time.Clock()
        self.tick = 0

    def check_proximity_and_create(self):
        new_entities = []
        for i in range(len(self.ai_entities)):
            mate = self.ai_entities[i].is_eligible_for_reproduction(self.ai_entities)
            if mate is not None:
                new_x = self.ai_entities[i].position[0] + 1
                new_y = self.ai_entities[i].position[1]
                new_color = [
                    (self.ai_entities[i].color[j] + mate.color[j]) // 2 for j in range(3)
                ]
                new_entity = AIEntity(new_x, new_y, new_color, 9)
                new_entities.append(new_entity)
                self.ai_entities[i].moves_since_last_reproduction = 0
        return new_entities

    def remove_older_entities_on_same_position(self):
        new_ai_entities = []
        for i in range(len(self.ai_entities)):
            younger_entity_on_same_position = False
            for j in range(len(self.ai_entities)):
                if i != j and self.ai_entities[i].position == self.ai_entities[j].position:
                    if self.ai_entities[i].is_younger_than(self.ai_entities[j]):
                        younger_entity_on_same_position = True
                        break
            if not younger_entity_on_same_position:
                new_ai_entities.append(self.ai_entities[i])
        self.ai_entities = new_ai_entities

    def main_loop(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()

            for ai_entity in self.ai_entities:
                ai_entity.ai_move()

            new_entities = self.check_proximity_and_create()
            self.ai_entities.extend(new_entities)

            self.remove_older_entities_on_same_position()

            self.ai_entities = [entity for entity in self.ai_entities if not entity.is_dead()]

            self.screen.fill((0, 0, 0))

            for ai_entity in self.ai_entities:
                ai_entity.draw(self.screen)

            pygame.display.flip()

            self.clock.tick(config.ticks)
            self.tick += 1;

if __name__ == '__main__':
    game = Game()
    game.main_loop()