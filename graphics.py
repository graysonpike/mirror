import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame

from time import gmtime, strftime
from datetime import date
import calendar

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Graphics:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = pygame.time.Clock()
        self.fullscreen = False

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

    def render(self, info):
        self.screen.fill(BLACK)

        # Weather
        self.render_text(self.THIN_HEADING, 100, 350, "Hello, %s" % info.name, hcenter=True)
        self.render_text(self.THIN_HEADING, 50, 50, "%s°" % info.weather['item']['condition']['temp'])
        self.render_text(self.SUBHEADING, 50, 130, "%s" % info.weather['item']['condition']['text'])
        
        # Clock / Date
        self.render_text(self.THIN_HEADING, self.width-42, 50, strftime("%-I:%M"), draw_from_left=True)
        self.render_text(self.SUBHEADING, self.width-50, 130, calendar.day_name[date.today().weekday()], draw_from_left=True)

        pygame.display.update()
        self.clock.tick(60)


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
