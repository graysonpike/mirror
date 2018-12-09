import os
os.environ['PYGAME_FREETYPE'] = '1'
import json
import pygame
from pygame.locals import *
from graphics import Graphics
from apis import get_weather


class Info:

    def __init__(self, json):
        self.name = json['name']
        self.woeid = json['woeid']
        self.weather = None


def main():
    
    graphics = Graphics(768, 1040)

    info_file = open('info.json')
    info = Info(json.load(info_file))

    info.weather = get_weather(info.woeid)
    
    loop = True
    while(loop):
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    loop = False
            elif event.type == KEYDOWN and event.key == K_RETURN:
                graphics.toggle_fullscreen()
        graphics.render(info)


main()
