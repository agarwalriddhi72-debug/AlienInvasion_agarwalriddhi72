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
        alien_w = self.settings.alien_w
        screen_w = self.settings.screen_w

        half_screen = screen_w // 2
        fleet_w, fleet_h = self.calculate_fleet_size(alien_h, half_screen, alien_w, screen_h)

        x_offset, y_offset = self.calculate_offsets(alien_h, screen_h, alien_w, fleet_w, fleet_h, half_screen)

        self._create_rectangle_fleet(alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset)

    def _create_rectangle_fleet(self, alien_h, alien_w, fleet_w, fleet_h, x_offset, y_offset):
        for col in range(fleet_w):
            for row in range(fleet_h):
                current_x = alien_w * col + x_offset
                current_y = alien_h * row + y_offset
                if col % 2 == 0 or row % 2 == 0:
                    continue
                self._create_alien(current_x, current_y)

    def calculate_offsets(self, alien_h, screen_h, alien_w, fleet_w, fleet_h, half_screen):
        fleet_vertical_space = fleet_h * alien_h
        fleet_horizontal_space = fleet_w * alien_w

        x_offset = half_screen + (half_screen - fleet_horizontal_space) // 2
        y_offset = int((screen_h - fleet_vertical_space) // 2)
        return x_offset, y_offset

    def calculate_fleet_size(self, alien_h, half_screen, alien_w, screen_h):
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
        """Create an alien and place it in the column."""
        new_alien = Alien(self, current_x, current_y)

        self.fleet.add(new_alien)
    
    def draw(self) -> None:
        """Draw the fleet to the screen."""
        alien: 'Alien'
        for alien in self.fleet:
            alien.draw_alien()

    def _check_fleet_edges(self):
        alien: Alien
        for alien in self.fleet:
            if alien.check_edges():
                self.fleet_direction *= -1
                self.drop_alien_fleet()
                break
            
    def drop_alien_fleet(self):
        alien: Alien
        for alien in self.fleet:
            alien.x -= self.fleet_drop_speed
            
    def update_fleet(self):
        self._check_fleet_edges()
        self.fleet.update()
        