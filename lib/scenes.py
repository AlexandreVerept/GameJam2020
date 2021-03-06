import pygame
import os


# Scene object
class Scene(object):
    def __init__(self, key, background=None, timer=False):
        self.key = key
        self.ticks = 0
        self.collection = None
        self.background = None
        self.width = 0
        self.height = 0

        (self.width, self.height) = pygame.display.get_surface().get_size()

        if background:
            self.background = pygame.image.load(os.path.join('assets', background))
            self.background = pygame.transform.scale(self.background, pygame.display.get_surface().get_size())

    def update_collection(self, collection):
        self.collection = collection

    def draw(self, win):
        if self.background:
            win.blit(self.background, (0, 0))

    def start(self, key):
        if self.collection:
            self.collection.set_active(key)
            self.collection.get(key).reset()

    def transit(self, transition_key, destination_key, ticks):
        self.collection.get(transition_key).set_destination(destination_key, ticks)
        self.start(transition_key)

    def reset(self):
        self.ticks = 0

    def update(self, mixer):
        (self.width, self.height) = pygame.display.get_surface().get_size()
        self.ticks = self.ticks + 1



class TransitionScene(Scene):
    def __init__(self, key, background=None):
        Scene.__init__(self, key, background)
        self.destination_key = False
        self.transit_ticks = -1

    def set_destination(self, key, ticks):
        self.destination_key = key
        self.transit_ticks = ticks

    def update(self, mixer):
        Scene.update(self, mixer)
        if 0 < self.transit_ticks <= self.ticks:
            if self.collection.get(self.destination_key):
                self.start(self.destination_key)
            else:
                self.start('splash')


# Scene collection object
class SceneCollection:
    def __init__(self):
        self.scenes = []
        self.active = False

    def append(self, scene):
        self.scenes.append(scene)

        for scene in self.scenes:
            scene.update_collection(self)

    def size(self):
        return len(self.scenes)

    def get(self, key):
        for scene in self.scenes:
            if scene.key == key:
                return scene

    def set_active(self, key):
        scene = self.get(key)

        if scene:
            self.active = scene

    def get_active(self):
        if not self.active:
            self.set_active('splash')
            return self.get_active()

        return self.active

    def get_keys(self):
        keys = []

        for scene in self.scenes:
            keys.append(scene.key)

        return keys
