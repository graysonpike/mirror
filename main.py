import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame
from pygame.locals import *
from graphics import Graphics


def main():
    
    graphics = Graphics(480, 640)
    
    loop = True
    while(loop):
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    loop = False
            elif event.type == KEYDOWN and event.key == K_RETURN:
                graphics.toggle_fullscreen()
        graphics.render()


main()
