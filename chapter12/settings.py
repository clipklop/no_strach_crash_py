#


class Settings():
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (230, 230, 230)

        # Ship settings
        self.ship_speed_factor = 10.5
        self.ship_limit = 3

        # Bullet settings
        self.bullet_speed_factor = 20.5
        self.bullet_width = 2
        self.bullet_height = 10
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 5

        # Alien settings
        self.alien_speed_factor = 10
        self.fleet_drop_speed = 10
        self.fleet_direction = 1