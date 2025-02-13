class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self):
        """Initialize the game's static settings."""
        # Screen settings
        self.screen_width = 1200
        self.screen_height = 800
        self.bg_color = (51, 0, 102)

        # Ship Settings
        self.ship_limit = 3

        # Bullet Settings
        self.bullet_width = 5
        self.bullet_height = 20
        self.bullet_color = (0, 179, 189)
        self.bullets_allowed = 10

        # Alien Settings
        self.fleet_drop_speed = 10

        # How quickly the game speeds up
        self.speedup_scale = 1.5
        # How quickly the alien point values increase
        self.score_scale = 1.5

        self.initialize_dynamic_settings()

    def initialize_dynamic_settings(self):
        """Initialize settings that will change during the course of the game."""
        self.ship_speed = 2.5
        self.bullet_speed = 1.5
        self.alien_speed = 1.0

        # Scoring Settings
        self.alien_points = 50

        # fleet_direction of 1 represents right; -1 represents left.
        self.fleet_direction = 1

    def increase_speed(self):
        """Increase the speed settings and alien point values."""
        self.ship_speed *= self.speedup_scale
        self.bullet_speed *= self.speedup_scale
        self.alien_speed *= self.speedup_scale

        self.alien_points = int(self.alien_points * self.score_scale)
