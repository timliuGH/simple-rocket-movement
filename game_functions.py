"""This module holds various game functions."""

import sys

import pygame

def check_keydown(event, rocket):
    """Respond to keypresses."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = True
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = True
    elif event.key == pygame.K_UP:
        rocket.moving_up = True
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = True

def check_keyup(event, rocket):
    """Respond to key releases."""
    if event.key == pygame.K_RIGHT:
        rocket.moving_right = False
    elif event.key == pygame.K_LEFT:
        rocket.moving_left = False
    elif event.key == pygame.K_UP:
        rocket.moving_up = False
    elif event.key == pygame.K_DOWN:
        rocket.moving_down = False

def check_events(rocket):
    """Respond to user events (keypresses, mouse clicks, etc)."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            check_keydown(event, rocket)
        elif event.type == pygame.KEYUP:
            check_keyup(event, rocket)

def update_screen(screen, settings, rocket):
    """Redraw and display game screen."""
    # Redraw the screen.
    screen.fill(settings.bg_color)
    rocket.blitme()

    # Make the most recently drawn screen visible.
    pygame.display.flip()
