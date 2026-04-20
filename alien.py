import pygame
from pygame.sprite import Sprite
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_fleet import AlienFleet

class Alien(Sprite):
    def __init__(self, fleet: 'AlienFleet', x: float, y: float) -> None:
        super().__init__()
        self.screen = fleet.screen
        self.boundaries = fleet.screen.get_rect()
        self.settings = fleet.settings

        self.image = pygame.image.load(self.settings.alien_file)
        self.image = pygame.transform.scale(self.image, (self.settings.alien_w, self.settings.alien_h))
        self.image = pygame.transform.rotate(self.image, -90)  # Rotate to face left towards the ship
        self.rect = self.image.get_rect()
        self.rect.x = self.boundaries.right - self.rect.width - x  # Position from the right side
        self.rect.y = y
        
        self.y = float(self.rect.y)
        self.x = float(self.rect.x)
    
    def update(self) -> None:
        temp_speed = self.settings.fleet_speed
        if self.check_edges():
            self.settings.fleet_direction *= -1
            self.x -= self.settings.fleet_drop_speed
        self.y += temp_speed * self.settings.fleet_direction
        self.rect.y = self.y
        self.rect.x = self.x

    def check_edges(self) -> bool:
        """Return True if alien is at edge of screen."""
        return (self.rect.bottom >= self.boundaries.bottom) or (self.rect.top <= self.boundaries.top)

    def draw_alien(self) -> None:
        self.screen.blit(self.image, self.rect)