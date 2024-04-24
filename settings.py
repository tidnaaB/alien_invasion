class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 0, 102)

        # Ship Settings
        self.ship_speed = 2.5
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_speed = 4.25
        self.bullet_width = 5
        self.bullet_height = 15
        self.bullet_color = (0, 179, 189)
        self.bullets_allowed = 10

        # Alien Settings
        self.alien_speed = 1.0
        self.fleet_drop_speed = 50
        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1
