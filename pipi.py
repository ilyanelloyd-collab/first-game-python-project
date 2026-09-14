import asyncio
import pygame

# Pygbag/browser: initialize pygame BEFORE importing game modules.
pygame.init()

from game import Game


async def main():
    clock = pygame.time.Clock()
    FPS = 60

    pygame.display.set_caption("la3bat scrims l m3argin ta5ser t5aless")

    # Use a 16:9 game surface so the browser does not add aspect-ratio bars.
    # The existing game logic still uses the same 2010px horizontal coordinates.
    screen = pygame.display.set_mode((2010, 1130))

    background = pygame.image.load('assets/bg.jpg')
    background = pygame.transform.scale(background, screen.get_size())
    banner = pygame.image.load('assets/banner.png')
    banner = pygame.transform.scale(banner, (750, 750))
    play_button = pygame.image.load('assets/button.png')
    play_button = pygame.transform.scale(play_button, (625, 200))
    play_button_rect = play_button.get_rect(topleft=(665, 500))

    game = Game()
    running = True

    while running:
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

        screen.blit(background, (0, 0))

        if game.is_playing:
            game.update(screen)
        else:
            screen.blit(play_button, play_button_rect)
            screen.blit(banner, (580, -60))

        pygame.display.flip()
        clock.tick(FPS)
        await asyncio.sleep(0)


asyncio.run(main())
