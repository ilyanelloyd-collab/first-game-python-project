import asyncio
import pygame
from game import Game

pygame.init()

async def main():
    clock = pygame.time.Clock()
    FPS = 180

    pygame.display.set_caption("la3bat scrims l m3argin ta5ser t5aless")
    screen = pygame.display.set_mode((2010, 1000))

    background = pygame.image.load('assets/bg.jpg')
    banner = pygame.image.load('assets/banner.png')
    banner = pygame.transform.scale(banner, (750, 750))
    play_button = pygame.image.load('assets/button.png')
    play_button = pygame.transform.scale(play_button, (625, 200))
    play_button_rect = play_button.get_rect(topleft=(665, 500))

    game = Game()
    running = True

    while running:
        screen.blit(background, (0, 0))

        if game.is_playing:
            game.update(screen)
        else:
            screen.blit(play_button, (665, 500))
            screen.blit(banner, (580, -60))

        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.KEYDOWN:
                game.pressed[event.key] = True

                if event.key == pygame.K_SPACE:
                    game.start()
                    game.sound_manager.play('click')
                elif event.key == pygame.K_a:
                    game.player.launch_projectile(-1)
                elif event.key == pygame.K_d:
                    game.player.launch_projectile(1)
            elif event.type == pygame.KEYUP:
                game.pressed[event.key] = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if play_button_rect.collidepoint(event.pos):
                    game.start()
                    game.sound_manager.play('click')

        clock.tick(FPS)
        await asyncio.sleep(0)

    pygame.quit()

asyncio.run(main())
