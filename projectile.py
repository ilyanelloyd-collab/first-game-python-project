import pygame

class projectile(pygame.sprite.Sprite):

    def __init__(self, player, direction, game):
        super().__init__()
        self.game = game
        self.velocity = 4
        self.player = player
        self.image = pygame.image.load('./assets/projectile.png')
        self.image = pygame.transform.scale(self.image, (40, 40))
        self.rect = self.image.get_rect()
        self.rect.x=player.rect.x + 175
        self.rect.y = player.rect.y + 75
        self.origin_image = self.image
        self.angle = 0
        self.direction = direction
        if self.direction == 1:
            self.rect.x = player.rect.x + 175
        else:
            self.rect.x = player.rect.x - 10


    def rotate(self):

        self.angle += 10
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)
        self.rect = self.image.get_rect(center=self.rect.center)

    def remove(self):
        self.player.all_projectile.remove(self)
        #self.Game.all_monsters.remove(self)

    def move(self):
        self.rect.x += self.velocity * self.direction
        self.rotate()

        for monster in self.game.check_collision(self, self.player.game.all_monsters):
            self.remove()
            monster.damage(self.player.attack)

        if self.rect.x > 1945:
            self.remove()
        elif self.rect.x < 0:
            self.remove()



