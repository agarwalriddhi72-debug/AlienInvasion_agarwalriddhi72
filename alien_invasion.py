"""
Program Name: Alien Invasion
Name: Riddhi Agarwal
Date: April 17, 2026
Purpose: An Alien Invasion game where the player controls a spaceship and shoots lasers at aliens. 
        The player can move the ship up and down and fire bullets to destroy the aliens. 
"""

import sys
import pygame
from settings import Settings
from ship import Ship
from arsenal import Arsenal
from alien import Alien

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
        pygame.display.set_caption(self.settings.name)

        self.bg = pygame.image.load(self.settings.bg_file)
        self.bg = pygame.transform.scale(self.bg, (self.settings.screen_w, self.settings.screen_h))

        self.running = True
        self.clock = pygame.time.Clock()

        pygame.mixer.init()
        self.laser_sound = pygame.mixer.Sound(self.settings.laser_sound)
        self.laser_sound.set_volume(0.7)

        self.ship = Ship(self, Arsenal(self))
        self.alien = Alien(self, 10, 10)  # Example alien for testing

    def run_game(self): 
        """Starts the main game loop."""
        # Game loop - check player position, enemy position, where laser should be
        while self.running:  
            self._check_events()
            self.ship.update()
            self.alien.update()
            self._update_screen()
            self.clock.tick(self.settings.FPS) 

    def _update_screen(self) -> None:
        """Updates the screen with the background and ship, then flips to the new screen."""
        self.screen.blit(self.bg, (0, 0))
        self.ship.draw()
        self.ship.arsenal.draw()
        self.alien.draw_alien()
        pygame.display.flip()

    def _check_events(self) -> None:
        """Checks for player input and handles events."""
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
                pygame.quit()
                sys.exit()
                
            elif event.type == pygame.KEYDOWN:
                self._check_keydown_events(event)
            elif event.type == pygame.KEYUP:
                self._check_keyup_events(event)

    def _check_keyup_events(self, event) -> None:
        """Checks when keys are released and updates ship movement accordingly."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = False
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = False

    
    def _check_keydown_events(self, event) -> None:
        """Checks when keys are pressed and updates ship movement or firing accordingly."""
        if event.key == pygame.K_UP:
            self.ship.moving_up = True
        elif event.key == pygame.K_DOWN:
            self.ship.moving_down = True
        elif event.key == pygame.K_SPACE:
            if self.ship.fire():
                self.laser_sound.play()
                self.laser_sound.fadeout(250)
        elif event.key == pygame.K_q:
            self.running = False
            pygame.quit()
            sys.exit()

if __name__ == '__main__':
    ai = AlienInvasion()
    ai.run_game()