"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the fleet of aliens in the game.
"""

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
        """Makes the fleet of aliens."""
        alien_h = self.settings.alien_h
        screen_h = self.settings.screen_h
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        half_screen = screen_w // 2
        fleet_w, fleet_h = self.calculate_fleet_size(alien_h, half_screen, alien_w, screen_h)

        x_offset, y_offset = self.calculate_offsets(alien_h, screen_h, alien_w, fleet_w, fleet_h, half_screen)

        self._create_rectangle_fleet(alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset):
        """Creates a rectangular fleet of aliens."""
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_h, screen_h, alien_w, fleet_w, fleet_h, half_screen):
        """Calculates the offsets in order to center the fleet."""
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_w

        x_offset = half_screen + (half_screen - fleet_horizontal_space) // 2
        y_offset = int((screen_h - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_h, half_screen, alien_w, screen_h):
        """Calculates the number of aliens that fit on the screen."""
        fleet_h = (screen_h // alien_h)
        fleet_w = (half_screen // alien_w)

        if fleet_h % 2 == 0:
            fleet_h -= 1
        else:
            fleet_h -= 2

        if fleet_w % 2 == 0:
            fleet_w -= 1
        else:
            fleet_w -= 2

        return fleet_w, fleet_h

    def _create_alien(self, current_x: int, current_y: int) -> None:
        """Creates an alien and adds it to the fleet."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)
    
    def draw(self) -> None:
        """Draw the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def _check_fleet_edges(self):
        """Checks if any aliens have reached an edge(boundary), and if so, the direction is reversed and the fleet drops down."""
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self.drop_alien_fleet()
                break
            
    def drop_alien_fleet(self):
        """Drops the fleet down by the fleet drop speed."""
        alien: Alien
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed
            
    def update_fleet(self):
        """Updates the fleet's position, checking for edges and dropping if necessary."""
        self._check_fleet_edges()
        self.fleet.update()
        

    def check_destroyed_status(self):
        """Checks if the fleet has been destroyed."""
        return not self.fleet

    def check_fleet_left(self):
        """Checks if the fleet has reached the left edge of the screen."""
        alien: Alien
        for alien in self.fleet:
            if alien.rect.left <= 0:
                return True
        return False
    
    def check_collisions(self, bullets):
        """Checks for collisions between the fleet and bullets."""
        collisions = pygame.sprite.groupcollide(self.fleet, bullets, True, True)
        return collisions