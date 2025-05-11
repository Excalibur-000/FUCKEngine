import uuid
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from scene import Scene

class Entity:
    def __init__(self):
        pass

    def initialise(self, scene: Scene):
        self.id = uuid.uuid4()
        scene.entities[self.id] = self

    def update(self):
        pass

