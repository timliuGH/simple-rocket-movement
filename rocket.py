"""This module holds the Rocket class."""

import pygame

class Rocket():
    """This is a model of a rocket"""

    def __init__(self, screen, settings):
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

        # Get game settings to access rocket settings.
        self.settings = settings

        # Get rocket's center position in decimal form.
        self.bmp_pos = float(self.bmp_rect.centerx)

    def move(self):
        """Move the ship based on movement flags."""
        # Update rocket's position, not the rect.
        if self.moving_right:
            #self.bmp_rect.centerx += 1
            self.bmp_pos += self.settings.rocket_speed
        # Use if instead of elif for smoother transition.
        # Pressing both keys keeps rocket still. 
        if self.moving_left:            
            #self.bmp_rect.centerx -= 1
            self.bmp_pos -= self.settings.rocket_speed

        # Update rect from bmp_pos
        self.bmp_rect.centerx = self.bmp_pos

    def blitme(self):
        """Draw rocket at current location."""
        self.screen.blit(self.bmp, self.bmp_rect)
