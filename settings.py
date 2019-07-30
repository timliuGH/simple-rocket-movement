"""This module holds the Settings class."""

class Settings():
    """This class holds the game settings."""

    def __init__(self):
        """Initialize game settings."""
        # Screen settings
        self.display_width = 1200
        self.display_height = 800
        self.display_caption = "Simple Rocket Movement"
        self.bg_color = (230, 230, 230)

        # Rocket settings
        self.rocket_speed = 1.5
