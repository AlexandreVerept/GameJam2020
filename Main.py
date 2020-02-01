import pygame
import os
import GameModule as gm
from random import randint
from GameNumber1 import spamGame

os.chdir(os.path.dirname(os.path.realpath(__file__)))

pygame.init()

win = pygame.display.set_mode((1024,640))

pygame.display.set_caption("Consequences")
clock = pygame.time.Clock()
objectList = []
gameList = [spamGame()]

def redrawGameWindow(objectList):
    for obj in objectList:
        obj.draw(win)
    pygame.display.update()

#mainloop
gameMenu = gm.Menu()
objectList.append(gameMenu)
run = True
inGame = False
while run:
    clock.tick(27)
    # quit
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    for obj in objectList:
        if not inGame:
            if isinstance(obj ,gm.Menu):
                #start button check
                inGame = obj.checkMenu()
                if inGame:
                    # choose minigame at random
                    objectList.append(gameList[randint(0,len(gameList)-1)])
        elif inGame:
            if isinstance(obj,gm.miniGame):
                finish = obj.play()
                if finish:
                    objectList.pop(objectList.index(obj))
                    objectList.append(gameList[randint(0,len(gameList)-1)])
                    obj.reset()

    redrawGameWindow(objectList)

pygame.quit()