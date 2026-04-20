"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the player's ship.
"""

import pygame
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class Ship:
    """Represents the player's ship in the game."""
    def __init__(self, game: 'AlienInvasion', arsenal: 'Arsenal') -> None:
        """Initializes the ship's position and settings."""
        self.game = game
        self.settings = game.settings
        self.screen = game.screen
        self.boundaries = self.screen.get_rect()

        self.image = pygame.image.load(self.settings.ship_file)
        self.image = pygame.transform.scale(self.image, (self.settings.ship_w, self.settings.ship_h))
        self.image = pygame.transform.rotate(self.image, -90)

        self.rect = self.image.get_rect()
        self.rect.midleft = self.boundaries.midleft
        self.moving_up = False
        self.moving_down = False
        self.y = float(self.rect.y)
        self.arsenal = arsenal
        
    def _center_ship(self):
        """Centers the ship on the left side of the screen."""
        self.rect.midleft = self.boundaries.midleft
        self.y = float(self.rect.y) 

    def update(self) -> None:
        """Updates the ship's position and arsenal."""
        self._update_ship_movement()
        self.arsenal.update_arsenal()

    def _update_ship_movement(self):
        """Updates the ship's position based on keys."""
        temp_speed = self.settings.ship_speed
        
        # Update position based on keys, but only if within boundaries
        if self.moving_up and self.rect.top > self.boundaries.top:
            self.y -= temp_speed
        if self.moving_down and self.rect.bottom < self.boundaries.bottom:
            self.y += temp_speed
        
        # Update rect position
        self.rect.y = self.y
    
    def draw(self) -> None:
        """Draw the ship at its current location."""
        self.screen.blit(self.image, self.rect)

    def fire(self) -> None:
        """Fires a bullet."""
        return self.arsenal.fire_bullet()
    
    def check_collisions(self, other_group) -> bool:
        """Checks for collisions with another group."""
        if pygame.sprite.spritecollideany(self, other_group):
            self._center_ship()
            return True
        return False