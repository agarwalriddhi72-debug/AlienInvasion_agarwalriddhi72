"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 17, 2026
Purpose: Represents a bullet fired by the player's ship.
"""

import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Bullet(Sprite):
    """Represents a bullet fired by the ship."""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the bullet's position and settings."""
        super().__init__()
        self.screen = game.screen
        self.settings = game.settings

        self.image = pygame.image.load(self.settings.bullet_file)
        self.image = pygame.transform.scale(self.image, (self.settings.bullet_w, self.settings.bullet_h))
        self.image = pygame.transform.rotate(self.image, -90)
        self.rect = self.image.get_rect()
        self.rect.midleft = game.ship.rect.midright
        self.x = float(self.rect.x)
    
    def update(self) -> None:
        """Moves the bullet up and down the screen."""
        self.x += self.settings.bullet_speed
        self.rect.x = self.x

    def draw_bullet(self) -> None:
        """Draws the bullet to the screen."""
        self.screen.blit(self.image, self.rect)