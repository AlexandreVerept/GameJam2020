import pygame
from lib.scenes import Scene
from lib.modules import ButtonImage


class GalleryScene(Scene):
    def __init__(self):
        Scene.__init__(self, 'gallery', 'menu_background.png')

        self.font_title = pygame.font.SysFont('comicsansms', 80)
        self.font_back = pygame.font.SysFont('comicsansms', 30)

        self.back = ButtonImage(100, 80, 'back.png', (130, 130), True)
        # self.back = ButtonImage(100, 500, 'back.png', 2, True)
        self.back_text = self.font_back.render("Back", True, (255, 255, 255))
        self.title = self.font_title.render("Gallery", True, (255, 255, 255))

    def draw(self, win):
        Scene.draw(self, win)
        self.back.draw(win)
        win.blit(self.back_text, self.back_text.get_rect(center=(100, 150)))
        win.blit(self.title, self.title.get_rect(center=(self.width/2, 200)))

    def update(self):
        Scene.update(self)

        if self.back.is_clicked():
            self.start('splash')