import pygame


class Gauge:
    def __init__(self, x, y, size=False, center=False, v_max=20):
        self.value = 0
        self.x = x
        self.y = y
        self.size = (50, 400)
        if size:
            self.size = size
        self.center = center
        self.max = v_max

    def increase(self, v=1):
        self.value += v

        if self.value > self.max:
            self.value = self.max

    def decrease(self, v=1):
        if self.value > 0:
            self.value -= v

    def is_full(self):
        return self.value >= self.max

    def reset(self):
        self.value = 0

    def draw(self, win):
        delta = self.value / self.max

        if self.center:
            pygame.draw.rect(win, (0, 240, 50), (self.x - self.size[0]/2, self.y - self.size[1]/2, self.size[0], self.size[1]))
            pygame.draw.rect(win, (0, 0, 0),
                             (self.x - self.size[0] / 2, self.y - self.size[1] / 2, self.size[0], self.size[1] * delta))
        else:
            pygame.draw.rect(win, (0, 240, 50), (self.x, self.y, self.size[0], self.size[1]))
            pygame.draw.rect(win, (0, 0, 0), (self.x, self.y, self.size[0], self.size[1] * delta))


class Cursor(object):
    def __init__(self, x, y, size=(5, 170), center=False):
        self.x = x
        self.y = y
        self.baseX = x
        self.baseY = y
        self.size = size
        self.center = center

    def slide(self, offset=5):
        if self.x <= 900:
            self.x += offset

    def reset(self):
        self.x = self.baseX
        self.y = self.baseY

    def draw(self, win):
        if self.x <= 900:
            if self.center:
                pygame.draw.rect(win, (40, 255, 40), (self.x - self.size[0]/2, self.y - self.size[1]/2, self.size[0], self.size[1]))
            else:
                pygame.draw.rect(win, (40, 255, 40),
                                 (self.x, self.y, self.size[0], self.size[1]))
