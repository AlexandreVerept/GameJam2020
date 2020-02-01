import pygame
import os

class Menu(object):
    def __init__(self):
        pygame.font.init()
        myfont = pygame.font.SysFont('Calibri', 72)
        self.title = myfont.render('Get your fix', False, (255, 255, 0))

        self.background = pygame.image.load(os.path.join('Ressources', 'menuBackGroundTest.jpg'))
        self.background = pygame.transform.scale(self.background, (1024,640))
        self.startButton = Button(100,100,72,72,"Start !")

    def draw(self,win):
        win.blit(self.background, (0,0))
        self.startButton.draw(win)
        win.blit(self.title,(1024/3,0))

    def checkMenu(self):
        return(self.startButton.checkClick())

class Button(object):

    def __init__(self,x,y,width,height,txt,pictureName=""):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.txt = txt
        # picture
        if pictureName:
            self.rect = None
            self.picture = pygame.image.load(os.path.join('Ressources', pictureName))
            self.picture = pygame.transform.scale(self.picture, (width, height))
        else:
            self.picture = None
            self.rect = pygame.Rect((x, y), (self.width, self.height))
    
    def draw(self,win):
        if self.picture:
            win.blit(self.picture, (self.x,self.y))
        else:
            pygame.draw.rect(win,(255,0,0),self.rect)
            font = pygame.font.SysFont("sans", 20)
            text = font.render(self.txt, True, (0,0,0))
            win.blit(text, (self.x,self.y))

    def checkClick(self):
        """
        Return True if press
        """
        if pygame.mouse.get_pressed()[0]:
            pos = pygame.mouse.get_pos()
            if pos[0]>self.x and pos[0]<self.x+self.width:
                if pos[1]>self.y and pos[1]<self.y+self.height:
                    return(True)
        return(False)

class miniGame(object):
    """
    every minigame need a draw and play method
    """
    def __init__(self):
        super.__init__()

class gauge(miniGame):
    def __init__(self,objectivNumber):
        self.objectivNumber = objectivNumber
        self.number = 0

    def draw(self,win):
        #front
        pygame.draw.rect(win,(0,240,50),(50,400,50,100))
        #back
        delta = self.number / self.objectivNumber * 100
        pygame.draw.rect(win,(0,0,0), pygame.Rect((50, 400), (50 , 100-delta)))

    def increase(self):
        self.number +=1
        if self.number > self.objectivNumber:
            self.number = self.objectivNumber

    def decrease(self):
        if self.number > 0:
            self.number -= 0.2

    def isFull(self):
        if self.number>=self.objectivNumber:
            return(True)
        else:
            return(False)