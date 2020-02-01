import pygame
import os
from GameModule import gauge,miniGame
from random import randint

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

class musicGame(miniGame):
    def __init__(self):
        self.count = 0
        self.background = pygame.image.load(os.path.join('Ressources', 'Concert_Chat_Triangle_Idle_Without_Note.jpg'))
        self.background = pygame.transform.scale(self.background, (1024,640))
        y = 640/4*3
        x = 1024/6
        self.notesPositions = [(x*2,y-randint(0,50)),(x*3,y-randint(0,50)),(x*4,y-randint(0,50)),(x*5,y-randint(0,50))]
        #notes
        self.notesPictures = {}
        self.notesPictures["black"] = pygame.image.load(os.path.join('Ressources', 'Note_Black.png'))
        self.notesPictures["red"] = pygame.image.load(os.path.join('Ressources', 'Note_Red.png'))
        self.notesPictures["yellow"] = pygame.image.load(os.path.join('Ressources', 'Note_Yellow.png'))
        for key in self.notesPictures.keys():
            self.notesPictures[key] = pygame.transform.scale(self.notesPictures[key], (36,80))
        self.redPosition = randint(1,3)
        #cursor
        self.cursor = cursor()

    def play(self):
        self.count += 1
        self.cursor.increase()
        if pygame.mouse.get_pressed()[0]:
            self.background = pygame.image.load(os.path.join('Ressources', 'Concert_Chat_Triangle_Action_Without_Note_ding.jpg'))
            self.background = pygame.transform.scale(self.background, (1024,640))
            if 130/4 * (self.redPosition+1)-20 <= self.count <= 130/4*(self.redPosition+1)+15:
                return(True)
            else:
                return(True)
        if self.count > 130:
            return(True)

    def reset(self):
        self.__init__()

    def draw(self,win):
        win.blit(self.background, (0,0))
        for i,p in enumerate(self.notesPositions):
            if i==self.redPosition:
                win.blit(self.notesPictures["red"], p)
            else:
                win.blit(self.notesPictures["black"], p)
        self.cursor.draw(win)

class cursor():
    def __init__(self):
        self.size = (5,170)
        self.y = 400
        self.x = 1024/4

    def increase(self):
        if self.x < 875:
            self.x += 5

    def draw(self,win):
        pygame.draw.rect(win,(40,255,40),pygame.Rect((self.x,self.y), self.size))