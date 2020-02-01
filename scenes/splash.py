import pygame
from lib.scenes import Scene


class SplashScene(Scene):
    def __init__(self):
        Scene.__init__(self, "splash", 'menu_background.png')

        self.font = pygame.font.SysFont("Arial", 80)
        self.title = self.font.render("Get Your Fix!", True, (255, 255, 255))

    def draw(self, win):
        Scene.draw(self, win)

        win.blit(self.title, self.title.get_rect(center=(self.width/2, self.height/2)))

    def update(self):
        Scene.update(self)

        # Change scene after 1 second
        if self.ticks > 6:
            self.start('other')


# Test scene
class Other(Scene):
    def __init__(self):
        Scene.__init__(self, "other", '2.png')
