import os
import pygame
from lib.scenes import TransitionScene


class TransitionLose(TransitionScene):
    def __init__(self):
        TransitionScene.__init__(self, 'trans_lose', 'menu_background.png')

        self.font_title = pygame.font.Font(os.path.join('assets', 'SigmarOne-Regular.ttf'), 80)

        self.title = self.font_title.render(":(", True, (255, 255, 255))

    def draw(self, win):
        TransitionScene.draw(self, win)
        win.blit(self.title, self.title.get_rect(center=(self.width / 2, self.height / 2)))


class TransitionWin(TransitionScene):
    def __init__(self):
        TransitionScene.__init__(self, 'trans_win', 'menu_background.png')

        self.font_title = pygame.font.Font(os.path.join('assets', 'SigmarOne-Regular.ttf'), 80)
        self.title = self.font_title.render('Continue !', True, (255, 255, 255))

    def draw(self, win):
        TransitionScene.draw(self, win)
        win.blit(self.title, self.title.get_rect(center=(self.width / 2, self.height / 2)))
