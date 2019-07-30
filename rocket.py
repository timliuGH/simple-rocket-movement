"""This module holds the Rocket class."""

import pygame

class Rocket():
    """This is a model of a rocket"""

    def __init__(self, screen):
        """Initialize the ship."""
        # Get game display and rocket image.
        self.screen = screen
        self.bmp = pygame.image.load('rocket.bmp')

        # Get rocket and screen rect.
        self.bmp_rect = self.bmp.get_rect()
        self.screen_rect = screen.get_rect()

        # Start rocket at bottom center of screen.
        self.bmp_rect.centerx = self.screen_rect.centerx
        self.bmp_rect.bottom = self.screen_rect.bottom

        # Movement flag
        self.moving_right = False
        self.moving_left = False

    def move(self):
        """Move the ship based on movement flags."""
        if self.moving_right:
            self.bmp_rect.centerx += 1
        # Use if instead of elif for smoother transition.
        # Pressing both keys keeps rocket still. 
        if self.moving_left:            
            self.bmp_rect.centerx -= 1

    def blitme(self):
        """Draw rocket at current location."""
        self.screen.blit(self.bmp, self.bmp_rect)
