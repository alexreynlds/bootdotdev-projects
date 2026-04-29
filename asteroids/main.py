import pygame
from player import Player
from constants import SCREEN_HEIGHT, SCREEN_WIDTH
from logger import log_state


def main():
    pygame.init()
    game_clock = pygame.time.Clock()
    delta_time = 0
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    player = Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    while True:
        log_state()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        screen.fill("black")

        player.update(delta_time)
        player.draw(screen)

        pygame.display.flip()

        delta_time = game_clock.tick(60) / 1000


if __name__ == "__main__":
    main()
