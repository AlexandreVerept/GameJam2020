import os
import math
import pygame


class ButtonImage(object):
    def __init__(self, x, y, picture, scale=False, center=False):
        self.x = x
        self.y = y
        self.scale = scale
        self.center = center

        self.picture = pygame.image.load(os.path.join('assets', picture))

        if scale:
            self.picture = pygame.transform.scale(self.picture, scale)

    def is_clicked(self):
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()

            if self.center:
                if self.x - self.picture.get_width()/2 <= pos[0] <= self.x + self.picture.get_width()/2:
                    if self.y - self.picture.get_height()/2 <= pos[1] <= self.y + self.picture.get_height()/2:
                        return True
            else:
                if self.x <= pos[0] <= self.x + self.picture.get_width():
                    if self.y <= pos[1] <= self.y + self.picture.get_height():
                        return True

        return False

    def draw(self, win):
        if self.center:
            win.blit(self.picture, self.picture.get_rect(center=(self.x, self.y)))
        else:
            win.blit(self.picture, (self.x, self.y))


class Timer(object):
    def __init__(self, x, y, size=50, center=False, timer_max=3):
        self.x = x
        self.y = y
        self.size = size
        self.center = center
        self.value = 0
        self.timer_max = timer_max

        self.font_timer = pygame.font.Font(os.path.join('assets', 'SigmarOne-Regular.ttf'), self.size)
        self.text_timer = self.font_timer.render(str(self.timer_max), True, (255, 255, 255))

    def draw(self, win):
        if self.is_over():
            return True

        value = math.ceil(self.timer_max - self.value)
        self.text_timer = self.font_timer.render(str(value), True, (255, 255, 255))

        if self.center:
            win.blit(self.text_timer, self.text_timer.get_rect(center=(self.x, self.y)))
        else:
            win.blit(self.text_timer, (self.x, self.y))

    def reset(self):
        self.value = 0

    def update(self):
        self.value += 1/60

    def is_over(self):
        return self.value >= self.timer_max
