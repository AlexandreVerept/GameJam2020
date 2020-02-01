import pygame
import os
from GameModule import gauge,miniGame

class spamGame(miniGame):
    def __init__(self):
        self.background = pygame.image.load(os.path.join('Ressources', 'menuBackGroundTest.jpg'))
        self.background = pygame.transform.scale(self.background, (1024,640))
        self.gauge = gauge(20)
        self.lastClic = False
        
    def draw(self,win):
        win.blit(self.background, (0,0))
        self.gauge.draw(win)

    def play(self):
        if not self.lastClic:
            if pygame.mouse.get_pressed()[0]:
                self.gauge.increase()
                self.lastClic = True
            else:
                self.gauge.decrease()
            if self.gauge.isFull():
                return(True)
        else:
            if not pygame.mouse.get_pressed()[0]:
                self.lastClic=False

    def reset(self):
        self.__init__()