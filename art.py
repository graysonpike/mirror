import math
import pygame


class Parametric:

	def __init__(self, screen, x, y):
		self.line_width = 3
		self.screen = screen
		self.t = 0
		self.x = x
		self.y = y
		self.speed = 1
		self.n_lines = 10
		self.line_separation = 100


	def x1(self):
		return math.sin(self.t) * 100 + math.sin(self.t * 2) * 20

	def y1(self):
		return math.cos(self.t) * 100

	def x2(self):
		return math.sin(self.t) * 200 + math.sin(self.t) * 2

	def y2(self):
		return math.cos(self.t/2) * 200 + math.cos(self.t / 1.2) * 20


	def render(self):
		self.t = pygame.time.get_ticks() * self.speed / 500

		for i in range(self.n_lines):
			color = 255 * i / self.n_lines
			pygame.draw.line(self.screen,
				(color, color, color), 
				(self.x + self.x1(), self.y + self.y1()),
				(self.x + self.x2(), self.y + self.y2()),
				self.line_width)
			self.t += self.line_separation / 500 * self.speed