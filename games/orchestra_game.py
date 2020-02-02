import pygame
import os
import math
from random import randint
from lib.scenes import Scene
from lib.modules import Timer
from lib.game_objects import Cursor


class OrchestraGame(Scene):
    def __init__(self):
        Scene.__init__(self, 'game1', 'orchestra_cat_idle.jpg')
        self.timer = Timer(990, 600, 80, True, 3)
        self.x = self.width / 6
        self.y = self.height * 3 / 4
        self.cursor = Cursor(256, 485, (5, 170), True)
        self.notes = []
        self.click = False
        self.won = False
        self.cling_start = False
        self.red_position = -1

        self.gen_notes()

        self.ding_background = pygame.image.load(os.path.join('assets', 'orchestra_cat_idle_ding.jpg'))
        self.ding_background = pygame.transform.scale(self.ding_background, pygame.display.get_surface().get_size())
        self.dong_background = pygame.image.load(os.path.join('assets', 'orchestra_cat_idle_ding_elephant.jpg'))
        self.dong_background = pygame.transform.scale(self.dong_background, pygame.display.get_surface().get_size())
        self.base_background = self.background

        self.cling_sound = pygame.mixer.Sound(os.path.join('assets', 'ding.wav'))
        self.clong_sound = pygame.mixer.Sound(os.path.join('assets', 'elephant.wav'))

        self.notes_pictures = {
            "black": pygame.transform.scale(pygame.image.load(os.path.join('assets', 'note_black.png')), (36, 80)),
            "red": pygame.transform.scale(pygame.image.load(os.path.join('assets', 'note_red.png')), (36, 80)),
            "yellow": pygame.transform.scale(pygame.image.load(os.path.join('assets', 'note_yellow.png')), (18, 40))
        }

    def gen_notes(self):
        self.notes = [
            (self.x * 2 - 25, self.y - randint(0, 80) + 40),
            (self.x * 3 - 25, self.y - randint(0, 80) + 40),
            (self.x * 4 - 25, self.y - randint(0, 80) + 40),
            (self.x * 5 - 25, self.y - randint(0, 80) + 40)
        ]

        self.red_position = randint(1, 3)

    def draw(self, win):
        Scene.draw(self, win)

        self.timer.draw(win)
        self.cursor.draw(win)

        for i, note in enumerate(self.notes):
            if i == self.red_position:
                win.blit(self.notes_pictures["red"], self.notes_pictures["red"].get_rect(center=note))
            else:
                win.blit(self.notes_pictures["black"], self.notes_pictures["black"].get_rect(center=note))

        if self.cling_start:
            if self.cling_start <= self.ticks <= self.cling_start + 30:
                if self.won:
                    self.background = self.ding_background
                else:
                    self.background = self.dong_background

                win.blit(self.notes_pictures["yellow"], (380, 140))
            else:
                self.background = self.base_background

    def cling(self):
        self.cling_start = self.ticks

    def cling_win(self):
        self.cling_sound.play()
        self.cling()

    def cling_lose(self):
        self.clong_sound.play()
        self.cling()

    def reset(self):
        Scene.reset(self)
        self.timer.reset()
        self.cursor.reset()
        self.gen_notes()
        self.background = self.base_background
        self.click = False
        self.won = False
        self.cling_start = False

    def update(self, mixer):
        Scene.update(self, mixer)

        if self.ticks <= 30:
            return True

        if not self.click:
            self.cursor.slide(randint(8, 20))

        self.timer.update()

        if self.timer.is_over():
            if self.won:
                self.transit('trans_win', 'game2', 45)
            else:
                self.transit('trans_lose', 'splash', 45)
            return True

        if not self.click:
            if pygame.mouse.get_pressed()[0]:
                self.click = True

                if abs(self.cursor.x - self.notes[self.red_position][0]) < 45:
                    self.won = True
                    self.cling_win()
                else:
                    self.cling_lose()
