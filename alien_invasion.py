"""
program's name:
Name: Riddhi
The purpose of the program: To create a game where the player controls a ship and shoots lasers at aliens.
Date: April 17, 2024
"""

import sys
import pygame

class AlienInvasion:
    """Main class to manage game assets and behavior."""
    def __init__(self) -> None:
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

        self.running = True

    def run_game(self): 
        # Game loop - check player position, enemy position, where laser should be
        while self.running:  
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            pygame.display.flip()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()