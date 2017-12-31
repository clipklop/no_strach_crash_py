#


import pygame
from pygame.sprite import Sprite


class Alien(Sprite):
    """Creates one Alien object."""
    def __init__(self, ai_settings, screen):
        """Initiates an alien and set its starting position."""
        super().__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Loads alien picture and rect attribute initialization
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Each new alien appears on the left top of the screen
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Saves precies position of an alien
        self.x = float(self.rect.x)

    def blitme(self):
        """Display alien in current position."""
        self.screen.blit(self.image, self.rect)