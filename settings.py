from pathlib import Path
class Settings:
    """A class to store all settings for Alien Invasion."""

    def __init__(self) -> None:
        """Initialize the game's settings."""
        self.name: str = "Alien Invasion"
        self.screen_w: int = 1200
        self.screen_h: int = 800
        self.FPS: int = 60
        self.bg_file = Path.cwd() / 'Assets' / 'images' / 'Starbasesnow.png'