"""
Program Name: Alien Invasion
Name: Riddhi Agarwal   
Date: April 19, 2026
Purpose: Represents the aliens in the game.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    """Represents a single alien in the fleet."""
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        """Initializes the alien's position and settings."""
        super().__init__()
        self.fleet = fleet
        self.screen = fleet.game.screen
        self.boundaries = fleet.game.screen.get_rect()
        self.settings = fleet.game.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.rotate(self.image, -90)  # Rotate to face left towards the ship
        self.rect = self.image.get_rect()
        self.rect.x = x  # Position from the right side
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self) -> None:
        """Updates the alien's position based on the fleet's movement."""
        temp_speed = self.settings.fleet_speed
        
        self.y += temp_speed * self.fleet.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if alien is at edge of screen."""
        return (self.rect.bottom >= self.boundaries.bottom) or (self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        """Draws the alien."""
        self.screen.blit(self.image, self.rect)