import os
import pygame
from lib.scenes import Scene
from lib.modules import ButtonImage


class SplashScene(Scene):
    def __init__(self):
        Scene.__init__(self, 'splash', 'background_yellow.png')

        self.gallery = ButtonImage(100, 550, 'gallery.png', (108, 108), True)
        self.start_button = ButtonImage(self.width / 2, self.height * 0.6, 'start.png', (500, 200), True)

        self.title = pygame.image.load(os.path.join('assets', 'title.png'))
        self.title = pygame.transform.scale(self.title, pygame.display.get_surface().get_size())

    def draw(self, win):
        Scene.draw(self, win)
        win.blit(self.title, self.title.get_rect(center=(self.width/2, self.height/2)))
        self.gallery.draw(win)
        self.start_button.draw(win)

    def update(self, mixer):
        Scene.update(self, mixer)

        if self.start_button.is_clicked():
            self.start('game0')

        if self.gallery.is_clicked():
            self.start('gallery')
