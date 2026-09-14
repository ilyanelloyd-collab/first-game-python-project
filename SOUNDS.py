import pygame


class SoundManager:
    def __init__(self, game):
        self.game = game
        self.sounds = {}

    def play(self, name):
        # Browsers can block audio until the first user interaction.
        # Never let an audio problem stop the game from rendering.
        try:
            if name not in self.sounds:
                self.sounds[name] = pygame.mixer.Sound(f'assets/sounds/{name}.ogg')
            self.sounds[name].play()
        except Exception:
            pass
