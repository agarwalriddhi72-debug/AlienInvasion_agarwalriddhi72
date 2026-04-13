import sys
import pygame
from settings import Settings
from ship import Ship

class AlienInvasion:
    """
    Main class for the Alien Invasion game.
    Responsible for:
    - Initializing the game
    - Running the main game loop
    - Handling events
    """

    def __init__(self) -> None:
        """Initializes the game, including settings, screen, background, and ship."""
        pygame.init()
        self.settings = Settings()

        self.screen = pygame.display.set_mode((self.settings.screen_w, self.settings.screen_h))
        pygame.display.set_caption("self.settings.name")

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        self.ship = Ship(self)

    def run_game(self): 
        """Starts the main game loop."""
        # Game loop - check player position, enemy position, where laser should be
        while self.running:  
            self._check_events()

            self._update_screen()
            self.clock.tick(self.settings.FPS) 

    def _update_screen(self) -> None:
        """Updates the screen with the background and ship, then flips to the new screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Checks for player input and handles events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()# Limit the frame rate to 60 frames per second

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()