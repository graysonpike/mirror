import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame
import calendar
import datetime
from art import Parametric, Rain, Snow


FPS = 60

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Graphics:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = pygame.time.Clock()
        self.fullscreen = False

        self.parametric = None

        self.HEADING = None
        self.SUBHEADING = None

        self.init()

    def init(self):
        pygame.init()
        pygame.font.init()

        self.screen = pygame.display.set_mode((self.width, self.height))

        self.HEADING = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Thin.otf", 64)
        self.THIN_HEADING = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Thin.otf", 32)
        self.SUBHEADING = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Thin.otf", 32)
        self.TEXT = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Regular.otf", 16)

        # self.parametric = Parametric(self.screen, self.width/2, self.height/2)
        self.snow = Snow(self.screen, self.width, self.height)
        self.rain = Rain(self.screen, self.width, self.height)

    def render(self, info):
        self.screen.fill(BLACK)

        # self.parametric.render()
        if info.snow_enabled:
            self.snow.render(self.clock.get_time())
        if info.rain_enabled:
            self.rain.render(self.clock.get_time())

        self.render_greeting(info)
        self.render_quote(info)
        self.render_weather(info)
        self.render_clock_and_date(info)
        self.render_forecast(info)


        pygame.display.update()

        self.clock.tick(FPS)


    def render_clock_and_date(self, info):
        self.render_text(self.THIN_HEADING, self.width-45, 50, info.time_string, draw_from_left=True)
        self.render_text(self.TEXT, self.width-50, 90, info.date_string, draw_from_left=True)


    def render_weather(self, info):
        self.render_text(self.THIN_HEADING, 50, 50, "%s°" % info.weather['current_observation']['condition']['temperature'])
        self.render_text(self.TEXT, 50, 90, "62°")
        self.render_text(self.TEXT, 80, 90, "75°")
        self.render_text(self.TEXT, 50, 110, "%s" % info.weather['current_observation']['condition']['text'])


    def render_forecast(self, info):
        forecast = info.weather['forecasts']
        offset = 0
        for day in forecast:
            self.render_text(self.TEXT, 107 + offset, self.height-160, day['day'][0])
            self.render_text(self.TEXT, 105 + offset, self.height-125, str(day['high']))
            self.render_text(self.TEXT, 105 + offset, self.height-100, str(day['low']))
            offset += 60
        # self.render_text(self.SUBHEADING, self.width-50, 130, info.date_string, draw_from_left=True)
        pass


    def render_greeting(self, info):
        salutation = None
        hour = datetime.datetime.now().hour
        if hour >= 4 and hour <= 11:
            salutation = "Good morning"
        if hour >= 12 and hour <= 18:
            salutation = "Good afternoon"
        else:
            salutation = "Good evening"
        self.render_text(self.THIN_HEADING, 0, 700, "%s, %s" % (salutation, info.name), hcenter=True)


    def render_quote(self, info):
        offset = 0 - len(info.quote_strings * 20)
        line_num = 0
        color = WHITE
        for line in info.quote_strings:
            if line_num == len(info.quote_strings) - 1:
                color = (100, 100, 100, 255)
            self.render_text(self.TEXT, 0, 820 + offset, info.quote_strings[line_num], hcenter=True, color=color)
            line_num += 1
            offset += 20


    def render_text(self, font, x, y, text, vcenter=False, hcenter=False, draw_from_left=False, color=WHITE):
        # Render text with anti-aliasing flag set
        surface = font.render(text, 1, color)
        if hcenter:
            x = self.width / 2 - surface.get_width() / 2
        if vcenter:
            y = self.height / 2 - surface.get_height() / 2
        if draw_from_left:
            x -= surface.get_width()
        self.screen.blit(surface, (x, y))


    def toggle_fullscreen(self):
        if self.fullscreen:
            pygame.display.set_mode((self.width, self.height))
            self.fullscreen = False
        else:
            pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            self.fullscreen = True
