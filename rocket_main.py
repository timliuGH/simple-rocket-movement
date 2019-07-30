import sys

import pygame

from settings import Settings
from rocket import Rocket
import game_functions as gf

def run_game():
    # Initialize game and settings. 
    pygame.init()
    settings = Settings()

    # Create game display.
    screen = pygame.display.set_mode(
        (settings.display_width, settings.display_height))
    pygame.display.set_caption(settings.display_caption)

    # Create rocket.
    rocket = Rocket(screen)

    # Start the main event loop for the game.
    while True:
        # Listen for keyboard and mouse events.
        gf.check_events()

        # Redraw the screen.
        screen.fill(settings.bg_color)
        rocket.blitme()

        # Make the most recently drawn screen visible.
        pygame.display.flip()

run_game()
