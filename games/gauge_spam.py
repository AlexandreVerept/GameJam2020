import os
import pygame
from lib.scenes import Scene
from lib.game_objects import Gauge
from lib.modules import Timer


class GaugeSpam(Scene):
    def __init__(self):
        Scene.__init__(self, 'game0', 'orchestra_dog.jpg')
        self.gauge = Gauge(100, self.height / 2, (50, 200), True, 5)
        self.timer = Timer(990, 600, 80, True, 3)
        self.click = False

        self.clap = pygame.image.load(os.path.join('assets', 'clap.png'))
        self.no_clap = pygame.image.load(os.path.join('assets', 'no_clap.png'))
        self.clap_sound = pygame.mixer.Sound(os.path.join('assets', 'clip.wav'))

        self.current_clap = self.no_clap

    def draw(self, win):
        Scene.draw(self, win)
        self.gauge.draw(win)
        self.timer.draw(win)
        win.blit(self.current_clap, self.current_clap.get_rect(center=(self.width/2, self.height * 3/4)))

    def reset(self):
        Scene.reset(self)
        self.gauge.reset()
        self.timer.reset()

    def update(self, mixer):
        Scene.update(self, mixer)
        self.timer.update()
        self.gauge.decrease(0.1)

        if self.timer.is_over():
            self.transit('trans_lose', 'splash', 45)
            return True

        if self.click:
            if not pygame.mouse.get_pressed()[0]:
                self.current_clap = self.no_clap
                self.click = False
        else:
            if pygame.mouse.get_pressed()[0]:
                self.gauge.increase(1.3)
                self.current_clap = self.clap
                self.clap_sound.play()
                self.click = True

        if self.gauge.is_full():
            self.transit('trans_win', 'game1', 45)
