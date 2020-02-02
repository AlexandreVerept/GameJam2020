import pygame
from lib.scenes import Scene
from lib.modules import ButtonImage


class SplashScene(Scene):
    def __init__(self):
        Scene.__init__(self, 'splash', 'menu_background.png')

        self.font_title = pygame.font.SysFont('comicsansms', 80)
        self.font_gallery = pygame.font.SysFont('comicsansms', 30)

        self.gallery = ButtonImage(100, 500, 'gallery.png', (156, 191), True)
        self.gallery_text = self.font_gallery.render("Gallery", True, (255, 255, 255))
        self.start_button = ButtonImage(self.width / 2, self.height * 0.6, 'start.png', (500, 200), True)
        self.title = self.font_title.render("Get Your Fix!", True, (255, 255, 255))

    def draw(self, win):
        Scene.draw(self, win)
        self.gallery.draw(win)
        self.start_button.draw(win)
        win.blit(self.gallery_text, self.gallery_text.get_rect(center=(100, 600)))
        win.blit(self.title, self.title.get_rect(center=(self.width/2, self.height/4)))

    def update(self, mixer):
        Scene.update(self, mixer)

        if self.start_button.is_clicked():
            self.start('game0')

        if self.gallery.is_clicked():
            self.start('gallery')
