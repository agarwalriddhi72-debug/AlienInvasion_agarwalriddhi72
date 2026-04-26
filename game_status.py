"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the game status
"""

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class GameStats():
    """Keeps track of game stats"""
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.reset_stats()

    def reset_stats(self) -> None:
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        #Update score
        self._update_score(collisions)
        #Update Max score
        self._update_max_score()
        #update hi score

    def _update_max_score(self) -> None:
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Max: {self.max_score}")

    def _update_score(self, collisions) -> None:
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f"Basic: {self.score}")
    
    def update_level(self) -> None:
        self.level += 1
        #print(f"Level: {self.level}")