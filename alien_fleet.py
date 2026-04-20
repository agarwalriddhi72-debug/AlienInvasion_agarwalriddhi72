import pygame
from typing import TYPE_CHECKING
from alien import Alien

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class AlienFleet:
    """Represents the fleet of aliens in the game."""
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.fleet = pygame.sprite.Group()
        self.fleet_direction = self.settings.fleet_direction
        self.fleet_drop_speed = self.settings.fleet_drop_speed

        self.create_fleet()

    def create_fleet(self) -> None:
        """Create the fleet of aliens."""
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        
        fleet_h = self.calculate_fleet_size(alien_h, screen_h)

        total_fleet_height = fleet_h * alien_h
        y_offset = (screen_h - total_fleet_height) // 2

        for row in range(fleet_h):
            current_y = alien_h * row + y_offset
            if row % 2 == 0:
                continue
            self._create_alien(0, current_y)  # x=0 positions at right edge

    def calculate_fleet_size(self, alien_size, screen_size):
        """Calculate the number of aliens that can fit."""
        fleet_size = (screen_size // alien_size)
        if fleet_size % 2 == 0:
            fleet_size -= 1
        else:
            fleet_size -= 2

        return fleet_size
    
    def _create_alien(self, current_x: int, current_y: int) -> None:
        """Create an alien and place it in the column."""
        new_alien = Alien(self.game, current_x, current_y)

        self.fleet.add(new_alien)
    
    def draw(self) -> None:
        """Draw the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def update(self) -> None:
        """Update the positions of all aliens in the fleet."""
        for alien in self.fleet:
            alien.update()