#


import pygame
from pygame.sprite import Sprite


class Bullet(Sprite):
	"""Class for managing a bullets fired up from a Ship."""
	def __init__(self, ai_settings, screen, ship):
		"""Makes an object of bullet in a current Ship's position."""
		super(Bullet, self).__init__()
		self.screen = screen

		# Makes a bullet in (0,0) position and changing it to correct one
		self.rect = pygame.Rect(0, 0, ai_settings.bullet_width, ai_settings.bullet_height)
		self.rect.centerx = ship.rect.centerx
		self.rect.top = ship.rect.top

		self.y = float(self.rect.y)

		self.color = ai_settings.bullet_color
		self.speed_factor = ai_settings.bullet_speed_factor
	
	def update(self):
		"""Moves bullet to the top of the screen."""
		# Updates position of the bullet in float value
		self.y -= self.speed_factor

		# Updates position of rectangle
		self.rect.y = self.y

	def draw_bullet(self):
		"""Dispaly bullet to the screen."""
		pygame.draw.rect(self.screen, self.color, self.rect)