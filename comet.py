import pygame
import random

import monster



class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.image = pygame.image.load('assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(3, 7)
        self.rect.x = random.randint(20, 2000)
        self.rect.y = -random.randint(0, 950)
        self.comet_event = comet_event

    def remove(self):
        self.comet_event.all_comets.remove(self)
        self.comet_event.game.sound_manager.play('meteorite')
        if len(self.comet_event.all_comets) == 0:
            print("fin event")
            self.comet_event.reset_percent()
            self.comet_event.game.spawn_monster(monster.mummy)
            self.comet_event.game.spawn_monster(monster.alien)


    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 710:
            print("pipi")
            self.remove()
            if len(self.comet_event.all_comets)== 0:
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            self.remove()
            self.comet_event.game.player.damage(20)

