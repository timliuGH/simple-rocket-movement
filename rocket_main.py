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
        gf.check_events()   # Listen for keyboard and mouse events.
        gf.update_screen()  # Redraw and display screen.  

run_game()
