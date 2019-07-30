"""This module holds various game functions."""

import sys

import pygame

def check_events():
    """Respond to user events (keypresses, mouse clicks, etc)."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()

def update_screen(screen, settings, rocket):
    """Redraw and display game screen."""
    # Redraw the screen.
    screen.fill(settings.bg_color)
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
