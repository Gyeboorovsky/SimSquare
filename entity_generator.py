import random

from ai_entity import AIEntity
from colors import red, blue, green


class EntityGenerator:
    def __init__(self):
        pass

    def create_entity(self, x, y, color):
        return AIEntity(x, y, color, random.randint(0, 9))

    def initial_state(self):
        ai_entities = []
        for i in range(5):
            ai_entities.append(AIEntity(i * 10, i * 10, red, 1))
            ai_entities.append(AIEntity(i * 10, 100 - i * 10, green, 2))
            ai_entities.append(AIEntity(100 - i * 10, i * 10, blue, 3))
        return ai_entities