import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame
import calendar
from art import Snow


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
        self.THIN_HEADING = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Ultralight.otf", 64)
        self.SUBHEADING = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Thin.otf", 32)
        self.TEXT = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Regular.otf", 16)

        # self.parametric = Parametric(self.screen, self.width/2, self.height/2)
        self.snow = Snow(self.screen, self.width, self.height)

    def render(self, info):
        self.screen.fill(BLACK)

        # Greeting
        self.render_text(self.THIN_HEADING, 100, 350, "Hello, %s" % info.name, hcenter=True)

        # self.parametric.render()
        self.snow.render(self.clock.get_time())

        self.render_weather(info)
        self.render_clock_and_date(info)
        self.render_forecast(info)

        pygame.display.update()

        self.clock.tick(FPS)


    def render_clock_and_date(self, info):
        self.render_text(self.THIN_HEADING, self.width-45, 50, info.time_string, draw_from_left=True)
        self.render_text(self.SUBHEADING, self.width-50, 130, info.date_string, draw_from_left=True)


    def render_weather(self, info):
        self.render_text(self.THIN_HEADING, 50, 50, "%s°" % info.weather['condition']['temp'])
        self.render_text(self.SUBHEADING, 50, 130, "62°")
        self.render_text(self.SUBHEADING, 110, 130, "75°")
        self.render_text(self.SUBHEADING, 50, 180, "%s" % info.weather['condition']['text'])


    def render_forecast(self, info):
        forecast = info.weather['forecast']
        offset = 0
        for day in forecast:
            self.render_text(self.TEXT, 107 + offset, self.height-160, day['day'][0])
            self.render_text(self.TEXT, 105 + offset, self.height-125, day['high'])
            self.render_text(self.TEXT, 105 + offset, self.height-100, day['low'])
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
