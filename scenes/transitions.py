import pygame
from lib.scenes import TransitionScene


class Transition1(TransitionScene):
    def __init__(self):
        TransitionScene.__init__(self, 'trans1', 'menu_background.png')

        self.font_title = pygame.font.SysFont('comicsansms', 80)

        self.title = self.font_title.render("Transition #1", True, (255, 255, 255))

    def draw(self, win):
        TransitionScene.draw(self, win)
        win.blit(self.title, self.title.get_rect(center=(self.width / 2, self.height / 2)))


class TransitionWin(TransitionScene):
    def __init__(self):
        TransitionScene.__init__(self, 'trans_win', 'menu_background.png')

        self.font_title = pygame.font.SysFont('comicsansms', 80)
        self.title = self.font_title.render('Continue !', True, (255, 255, 255))

    def draw(self, win):
        TransitionScene.draw(self, win)
        win.blit(self.title, self.title.get_rect(center=(self.width / 2, self.height / 2)))
