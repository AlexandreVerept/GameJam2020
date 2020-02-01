import os
import pygame
from lib.scenes import SceneCollection
from scenes.splash import SplashScene
from scenes.gallery import GalleryScene

SCREEN_SIZE = (1024, 640)

# Set working dir
os.chdir(os.path.dirname(os.path.realpath(__file__)))

# Init game
pygame.init()
clock = pygame.time.Clock()

# Main game window
win = pygame.display.set_mode(SCREEN_SIZE)
pygame.display.set_caption("Get Your Fix!")

# Init
run = True
started = False

# Create and fill SceneCollection
scenes = SceneCollection()
scenes.append(SplashScene())
scenes.append(GalleryScene())


# Main loop
while run:
    clock.tick(60)

    # Check for quit event
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    # Get active scene
    scene = scenes.get_active()

    # Update scene and draw it
    scene.update()
    scene.draw(win)
    pygame.display.update()


pygame.quit()
