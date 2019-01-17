import os
os.environ['PYGAME_FREETYPE'] = '1'
import json
import pygame
from datetime import datetime, date
from time import strftime, sleep
import calendar
from pygame.locals import *
from graphics import Graphics
from apis import get_weather

ordinal = lambda n: "%d%s" % (n,"tsnrhtdd"[(n/10%10!=1)*(n%10<4)*n%10::4])


class Info:

    def __init__(self, json):
        self.name = json['name']
        self.woeid = json['woeid']
        self.yahoo_client_key = json['yahoo_client_key']
        self.yahoo_client_secret = json['yahoo_client_secret']
        self.weather = None
        self.date_string = None
        self.time_string = None
        self.snow_enabled = False
        self.rain_enabled = False


def main():
    
    graphics = Graphics(768, 1024)

    info_file = open('info.json')
    info = Info(json.load(info_file))

    info.weather = get_weather(info.woeid, info.yahoo_client_key, info.yahoo_client_secret)
    
    last_minute = -1

    loop = True
    while(loop):
        for event in pygame.event.get():
            if event.type == QUIT or \
                (event.type == KEYDOWN and event.key == K_ESCAPE):
                    loop = False
            if event.type == KEYDOWN:
                if event.key == K_s:
                    info.snow_enabled = not info.snow_enabled
                if event.key == K_r:
                    info.rain_enabled = not info.rain_enabled
                if event.key == K_RETURN:
                    graphics.toggle_fullscreen()
        now = datetime.now()
        if last_minute != now.minute and (now.minute == 0 or last_minute == -1):
            info.weather = get_weather(info.woeid, info.yahoo_client_key, info.yahoo_client_secret)
            sleep(0.01)
            info.time_string = strftime("%-I:%M")
            info.date_string = calendar.day_name[date.today().weekday()] + ", " + calendar.month_abbr[date.today().month] + " " + ordinal(date.today().day)
            last_minute = now.minute
        graphics.render(info)


main()
