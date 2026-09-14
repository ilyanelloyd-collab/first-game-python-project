import pygame

from SOUNDS import SoundManager
from player import player
from monster import Monster, mummy, alien
from comet_event import CometFaLLEvent
class Game:
    def __init__(self):
        self.is_playing = False
        self.all_players = pygame.sprite.Group()
        self.player = player(self)
        self.all_players.add(self.player)
        self.comet_event = CometFaLLEvent(self)
        self.all_monsters = pygame.sprite.Group()
        self.sound_manager = SoundManager(self)
        self.font = pygame.font.SysFont("arial", 25)
        self.score = 0
        self.pressed = {}

    def game_over(self):
        self.all_monsters = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.comet_event.all_comets =  pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')
    def start(self):
        self.is_playing = True
        self.spawn_monster(mummy)
        self.spawn_monster(mummy)
        self.spawn_monster(alien)

    def add_score(self, points=10):
        self.score += points
    def update(self, screen):
        score_text = self.font.render("Score: " + str(self.score), 1, (0, 0, 0))

        screen.blit(score_text, (20, 20))

        screen.blit(self.player.image, self.player.rect)

        self.player.update_health_bar(screen)

        self.comet_event.update_bar(screen)

        self.player.update_animation()

        self.all_monsters.draw(screen)

        self.comet_event.all_comets.draw(screen)

        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monsters:
            monster.forward()
            monster.update(screen)
        for comet in self.comet_event.all_comets:
            comet.fall()

        self.player.all_projectile.draw(screen)

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x <= 1850:
            self.player.move_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x >= -35:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self, monster_class_name):
        self.all_monsters.add(monster_class_name.__call__(self))



