import pygame
import random


class AnimateSprite(pygame.sprite.Sprite):
    animations = {}

    def __init__(self, name, size=(200, 200)):
        super().__init__()
        self.size = size

        # Load animation frames only after pygame/display initialization.
        # Loading them at class-import time can stop Pygbag before the first frame.
        if name not in self.animations:
            self.animations[name] = self.load_animation_images(name)

        self.image = pygame.image.load(f'assets/{name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0
        self.images = self.animations[name]
        self.animation = False

    def start_animation(self):
        self.animation = True

    def animate(self, loop=False):
        if self.animation:
            self.current_image += random.randint(0, 1)
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    self.animation = False
            self.image = self.images[self.current_image]
            self.image = pygame.transform.scale(self.image, self.size)

    @staticmethod
    def load_animation_images(name):
        images = []
        path = f'assets/{name}/{name}'

        for num in range(1, 25):
            image_path = path + str(num) + '.png'
            images.append(pygame.image.load(image_path))

        return images
