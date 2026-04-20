"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 19, 2026
Purpose: Represents the game status
"""

#Volatile Game Stats

class GameStats():
    """Keeps track of game stats, such as remaining ships."""
    def __init__(self, ship_limit)-> None:
        self.ships_left = ship_limit