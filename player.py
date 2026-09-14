import pygame
from projectile import projectile
import animation
import time

class player(animation.AnimateSprite):
    def __init__(self, game):
        self.game = game
        super().__init__('player')
        self.health = 100
        self.max_health = 100
        self.attack = 50
        self.velocity = 2
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 435
        self.rect.y = 700
        self.last_shot_time = 0
        self.cooldown = 0.3
    def launch_projectile(self, direction):
        current_time = time.time()
        if  current_time - self.last_shot_time >= self.cooldown:
         self.all_projectile.add(projectile(self, direction, self.game))
         self.last_shot_time = current_time
         self.start_animation()
         self.game.sound_manager.play('tir')

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        pygame.draw.rect(surface, (0, 0 ,0) , [self.rect.x + 50, self.rect.y + 20, self.max_health, 7])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 7])
    def damage(self, amount):
        if self.health - amount  > amount:
         self.health -= amount
        else:
         self.game.game_over()

    def move_right(self):
        if not self.game.check_collision(self, self.game.all_monsters):
         self.rect.x += self.velocity
    def move_left(self):
        self.rect.x -= self.velocity