from . import scene

class Main:
    def __init__(self):
        self.scenes = {}

    def add_scene(self, scene: scene.Scene):
        self.scenes[scene.name] = scene

    def del_scene(self, name: str):
        del self.scenes[name]

    def run(self):
        pass