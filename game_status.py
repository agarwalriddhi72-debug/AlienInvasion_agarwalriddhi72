"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the game status
"""

#from pathlib import Path
import json
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from alien_invasion import AlienInvasion
    from arsenal import Arsenal

class GameStats():
    """Keeps track of game stats"""
    def __init__(self, game: 'AlienInvasion') -> None:
        """Initializes the game stats, including score, level, and ships left."""
        self.game = game
        self.settings = game.settings
        self.max_score = 0
        self.init_saved_scores()
        self.reset_stats()

    def init_saved_scores(self):
        """Initializes the max score and hi score from the scores file"""
        self.path = self.settings.scores_file
        if self.path.exists() and self.path.stat.__sizeof__() > 20:
            contents = self.path.read_text()
            scores = json.loads(contents)
            self.hi_score = scores.get('hi_score', 0)
        else:
            self.hi_score = 0
            self.save_scores()
            # Save the file

    def save_scores(self):
        """Saves the hi score to the scores file"""
        scores = {
            'hi_score': self.hi_score
        }
        contents = json.dumps(scores, indent = 4)
        try:
            self.path.write_text(contents)
        except FileNotFoundError as e:
            print(f"File Not Found: {e}")

    def reset_stats(self) -> None:
        """Resets the game stats to their initial values."""
        self.ships_left = self.settings.starting_ship_count
        self.score = 0
        self.level = 1

    def update(self, collisions) -> None:
        """Updates the score, max score, and hi score based on the collisions that occurred."""
        #Update score
        self._update_score(collisions)
        #Update Max score
        self._update_max_score()
        #update hi score
        self._update_hi_score()

    def _update_max_score(self) -> None:
        """Updates the max score if the current score exceeds it."""
        if self.score > self.max_score:
            self.max_score = self.score
        #print(f"Max: {self.max_score}")
    
    def _update_hi_score(self) -> None:
        """Updates the hi score if the current score exceeds it."""
        if self.score > self.hi_score:
            self.hi_score = self.score
        #print(f"Hi: {self.hi_score}")

    def _update_score(self, collisions) -> None:
        """Updates the score based on the number of aliens destroyed in the collisions."""
        for alien in collisions.values():
            self.score += self.settings.alien_points
        #print(f"Basic: {self.score}")
    
    def update_level(self) -> None:
        """Increases the level by 1."""
        self.level += 1
        #print(f"Level: {self.level}")