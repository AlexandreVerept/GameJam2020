import pygame
from lib.scenes import Scene
from lib.game_objects import Gauge
from lib.modules import Timer


class GaugeSpam(Scene):
    def __init__(self):
        Scene.__init__(self, 'game0', 'menu_background.png')
        self.gauge = Gauge(100, self.height / 2, (50, 200), True, 5)
        self.timer = Timer(990, 600, 80, True, 3)
        self.click = False

    def draw(self, win):
        Scene.draw(self, win)
        self.gauge.draw(win)
        self.timer.draw(win)

    def reset(self):
        Scene.reset(self)
        self.gauge.reset()
        self.timer.reset()

    def update(self, mixer):
        Scene.update(self, mixer)
        self.timer.update()
        self.gauge.decrease(0.1)

        if self.timer.is_over():
            self.transit('trans1', 'splash', 45)
            return True

        if self.click:
            if not pygame.mouse.get_pressed()[0]:
                self.click = False
        else:
            if pygame.mouse.get_pressed()[0]:
                self.gauge.increase(1.3)
                self.click = True

        if self.gauge.is_full():
            self.transit('trans1', 'game0', 45)
