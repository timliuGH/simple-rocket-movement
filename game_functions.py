"""This module holds various game functions."""

import sys

import pygame

def check_events():
    """Respond to user events (keypresses, mouse clicks, etc)."""
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            sys.exit()
