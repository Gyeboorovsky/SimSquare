from ai_entity import AIEntity
from colors import red, blue, green


class EntityGenerator:
    def __init__(self):
        pass

    def create_entity(self, x, y, color):
        return AIEntity(x, y, color)

    def initial_state(self):
        ai_entities = []
        for i in range(5):
            ai_entities.append(AIEntity(i * 10, i * 10, red))
            ai_entities.append(AIEntity(i * 10, 100 - i * 10, green))
            ai_entities.append(AIEntity(100 - i * 10, i * 10, blue))
        return ai_entities