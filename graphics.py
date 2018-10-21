import os
os.environ['PYGAME_FREETYPE'] = '1'
import pygame

WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


class Graphics:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.screen = None
        self.clock = pygame.time.Clock()
        self.fullscreen = False

        self.TEXT = None

        self.init()

    def init(self):
        pygame.init()
        pygame.font.init()
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.TEXT = pygame.font.Font("res/fonts/SanFran/SanFranciscoDisplay-Thin.otf", 64)

    def render(self):
        self.screen.fill(BLACK)
        self.render_text(self.TEXT, 100, 100, "Hello, Riddhi", hcenter=True)
        pygame.display.update()
        self.clock.tick(60)


    def render_text(self, font, x, y, text, vcenter=False, hcenter=False):
        # Render text with anti-aliasing flag set
        surface = font.render(text, 1, WHITE)
        if hcenter:
            x = self.width / 2 - surface.get_width() / 2
        self.screen.blit(surface, (x, y))


    def toggle_fullscreen(self):
        if self.fullscreen:
            pygame.display.set_mode((self.width, self.height))
            self.fullscreen = False
        else:
            pygame.display.set_mode((self.width, self.height), pygame.FULLSCREEN)
            self.fullscreen = True
