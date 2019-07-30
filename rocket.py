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
        self.moving_up = False
        self.moving_down = False

        # Get game settings to access rocket settings.
        self.settings = settings

        # Get rocket's position in decimal form.
        self.bmp_posx = float(self.bmp_rect.centerx)
        self.bmp_posy = float(self.bmp_rect.y)

    def move(self):
        """Move the ship based on movement flags."""
        # Update rocket's position, not the rect.
        # Check if reached end of game display.
        if self.moving_right and self.bmp_rect.right < self.screen_rect.right:
            #self.bmp_rect.centerx += 1
            self.bmp_posx += self.settings.rocket_speed
        # Use if instead of elif for smoother transition.
        if self.moving_left and self.bmp_rect.left > 0:            
            #self.bmp_rect.centerx -= 1
            self.bmp_posx -= self.settings.rocket_speed
        if self.moving_up and self.bmp_rect.top > 0:
            self.bmp_posy -= self.settings.rocket_speed
        if self.moving_down and self.bmp_rect.bottom < self.screen_rect.bottom:
            self.bmp_posy += self.settings.rocket_speed

        # Update rect from bmp_posx
        self.bmp_rect.centerx = self.bmp_posx
        self.bmp_rect.y = self.bmp_posy

    def blitme(self):
        """Draw rocket at current location."""
        self.screen.blit(self.bmp, self.bmp_rect)
