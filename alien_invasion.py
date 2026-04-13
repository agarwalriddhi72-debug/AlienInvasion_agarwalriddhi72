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
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False
                    pygame.quit()
                    sys.exit()

            self.screen.blit(self.bg, (0, 0))
            self.ship.draw()
            pygame.display.flip()
            self.clock.tick(self.settings.FPS) # Limit the frame rate to 60 frames per second

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()