import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from entity import Entity

class Scene:
    def __init__(self, name):
        self.name = name
        self.entities: dict[str, Entity] = {}

    def add(self, entity: Entity):
        entity.initialise(self)

    def remove(self, id: uuid.UUID):
        del self.entities[id]

    def update(self):
        for entity in self.entities:
            self.entities[entity].update()