import pygame
import random
import animation
class Monster(animation.AnimateSprite):
    def __init__(self, game, name, size, offset=0):
        super().__init__(name, size)
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.04
        self.rect = self.image.get_rect()
        self.rect.x = 1940 + random.randint(0, 300)
        self.rect.y = 740 - offset
        self.loot_amount = 10
        self.start_animation()

    def set_speed(self, speed):
        self.default_speed = speed
        self.velocity = random.randint(1, 3)

    def set_loot_amount(self, amount):
        self.loot_amount = amount

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
           self.rect.x = 1940 + random.randint(0, 300)
           self.velocity = random.randint(1, self.default_speed)
           self.health = self.max_health
           self.game.add_score (self.loot_amount)
           if self.game.comet_event.is_full_loaded():
               self.game.all_monsters.remove(self)
               self.game.comet_event.attempt_fall()




    def update(self, surface):
        pygame.draw.rect(surface, (0, 0 ,0) , [self.rect.x + 10, self.rect.y - 10, self.max_health, 5])
        pygame.draw.rect(surface, (11, 210, 46), [self.rect.x + 10, self.rect.y - 10, self.health, 5])
        self.animate(loop=True)

    def forward(self):
        if not self.game.check_collision(self, self.game.all_players):
         self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

class mummy(Monster):
    def __init__(self, game):
        super().__init__(game, "mummy", (130, 130))
        self.set_speed(3)
        self.set_loot_amount = 20

class alien(Monster):
    def __init__(self, game):
        super().__init__(game, "alien", (300, 300), 120)
        self.health = 250
        self.max_health = 250
        self.attack = 0.08
        self.set_speed(1)
        self.set_loot_amount = 80

