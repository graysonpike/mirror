import math
import pygame
from random import randint

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
		self.t = pygame.time.get_ticks() / 500 * self.speed

		for i in range(self.n_lines):
			color = 255 * i / self.n_lines
			pygame.draw.line(self.screen,
				(color, color, color), 
				(self.x + self.x1(), self.y + self.y1()),
				(self.x + self.x2(), self.y + self.y2()),
				self.line_width)
			self.t += self.line_separation / 500 * self.speed


class Parametric2:

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
		ticks = pygame.time.get_ticks()
		self.t = ticks / 500 * self.speed

		for i in range(self.n_lines):
			color = 255 * i / self.n_lines
			pygame.draw.line(self.screen,
				(color, color, color), 
				(self.x + self.x1(), self.y + self.y1()),
				(self.x + self.x2(), self.y + self.y2()),
				self.line_width)
			self.t += self.line_separation / 500 * self.speed

		self.t = ticks / 500 * self.speed + (math.pi)
		for i in range(self.n_lines):
			color = 255 * i / self.n_lines
			pygame.draw.line(self.screen,
				(color, color, color), 
				(self.x + self.x1(), self.y + self.y1()),
				(self.x + self.x2(), self.y + self.y2()),
				self.line_width)
			self.t += self.line_separation / 500 * self.speed



class Snow():

	class Flake():

		def __init__(self, width, height):
			self.x = randint(0, width)
			self.y = randint(0, height)
			self.vx = randint(1, 5)
			self.vy = randint(5, 10)
			self.color = randint(30, 60)
			self.width = width
			self.height = height
			self.line_width = 2

		def clamp(self):
			if self.x > self.width:
				self.x = 0
			if self.y > self.height:
				self.y = 0

		def render(self, screen, delta):
			self.x += self.vx * delta / 100
			self.y += self.vy * delta / 100
			self.clamp()
			pygame.draw.line(screen,
			(self.color, self.color, self.color),
			(self.x, self.y),
			(self.x + 2, self.y + 4),
			self.line_width)
			

	def __init__(self, screen, width, height):
		self.screen = screen
		self.width = width
		self.height = height
		self.n_drops = 100
		self.drops = []
		self.init_drops()

	def init_drops(self):
		for i in range(self.n_drops):
			self.drops.append(self.Flake(self.width, self.height))

	def render(self, delta):
		for drop in self.drops:
			drop.render(self.screen, delta)


class Rain():

	class Drop():

		def __init__(self, width, height):
			self.x = randint(0, width)
			self.y = randint(0, height)
			self.vx = 1
			self.vy = randint(8, 10)
			self.color = randint(50, 75)
			self.width = width
			self.height = height
			self.line_width = 2

		def clamp(self):
			if self.x > self.width:
				self.x = 0
			if self.y > self.height and randint(0,4) == 4:
				self.x = randint(0, self.width)
				self.y = 0

		def render(self, screen, delta):
			self.x += self.vx * delta / 10
			self.y += self.vy * delta / 10
			self.clamp()
			pygame.draw.line(screen,
			(self.color, self.color, self.color),
			(self.x, self.y),
			(self.x + 1, self.y + 10),
			self.line_width)
			

	def __init__(self, screen, width, height):
		self.screen = screen
		self.width = width
		self.height = height
		self.n_drops = 50
		self.drops = []
		self.init_drops()

	def init_drops(self):
		for i in range(self.n_drops):
			self.drops.append(self.Drop(self.width, self.height))

	def render(self, delta):
		for drop in self.drops:
			drop.render(self.screen, delta)
