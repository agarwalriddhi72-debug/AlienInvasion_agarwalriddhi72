import pygame
from bullet import Bullet
from typing import TYPE_CHECKING
if TYPE_CHECKING:
    from alien_invasion import AlienInvasion

class Arsenal:
    """Represents the ship's arsenal."""
    def __init__(self, game: 'AlienInvasion') -> None:
        self.game = game
        self.settings = game.settings
        self.arsenal = pygame.sprite.Group()

    def update_arsenal(self) -> None:
        """Updates the position of lasers and gets rid of old lasers."""
        self.arsenal.update()
        self._remove_bullets_offscreen()
    
    def _remove_bullets_offscreen(self) -> None:
        screen_rect = self.game.screen.get_rect()
        for bullet in self.arsenal.copy():
            if bullet.rect.left >= screen_rect.right:
                self.arsenal.remove(bullet)

    def draw(self) -> None:
        """Draws the bullets to the screen."""
        for bullet in self.arsenal:
            bullet.draw_bullet()

    def fire_bullet(self) -> bool:
        """Fires a bullet if limit not reached."""
        if len(self.arsenal) < self.settings.bullet_amount:
            new_bullet = Bullet(self.game)
            self.arsenal.add(new_bullet)
            return True
        return False