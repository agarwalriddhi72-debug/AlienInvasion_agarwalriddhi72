"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the game settings for Alien Invasion.
"""

from pathlib import Path
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1000
        self.screen_h: int = 500
        self.FPS: int = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'

        self.ship_file = Path.cwd() / 'Assets' / 'images' / 'ship2(no bg).png'
        self.ship_w = 40
        self.ship_h = 60
        self.ship_speed = 5

        self.bullet_file = Path.cwd() / 'Assets' / 'images' / 'laserBlast.png'
        self.laser_sound = Path.cwd() / 'Assets' / 'sound' / 'laser.mp3'
        self.impact_sound = Path.cwd() / 'Assets' / 'sound' / 'impactSound.mp3'
        self.bullet_speed = 7
        self.bullet_w = 25
        self.bullet_h = 80
        self.bullet_amount = 5

        self.alien_file = Path.cwd() / 'Assets' / 'images' / 'enemy_4.png' 
        self.alien_w = 40
        self.alien_h = 40
        self.fleet_speed = 3
        self.fleet_direction = 1
        self.fleet_drop_speed = 20

        self.starting_ship_count = 3

        self.button_w = 200
        self.button_h = 50
        self.button_color = (0, 135, 50)

        self.text_color = (255, 255, 255)
        self.button_font_size = 48
        self.HUD_font_size = 20
        self.font_file = Path.cwd() / 'Assets' / 'fonts' / 'Silkscreen' / 'Silkscreen-Bold.ttf'