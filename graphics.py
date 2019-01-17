import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame
import calendar
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

        # Greeting
        self.render_text(self.THIN_HEADING, 100, 700, "Hello, %s" % info.name, hcenter=True)

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


    def render_text(self, font, x, y, text, vcenter=False, hcenter=False, draw_from_left=False):
        # Render text with anti-aliasing flag set
        surface = font.render(text, 1, WHITE)
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
