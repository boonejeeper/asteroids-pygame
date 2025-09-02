import pygame
from pygame import Color

from asteroid import Asteroid
from asteroidfield import AsteroidField
from constants import SCREEN_WIDTH, SCREEN_HEIGHT
from player import Player


def main():
    pygame.init()
    screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

    # setup timing
    clock = pygame.time.Clock()
    dt = 0

    # set up groups
    updatable = pygame.sprite.Group()
    drawable = pygame.sprite.Group()
    asteroids = pygame.sprite.Group()

    Player.containers = (updatable, drawable)

    Asteroid.containers = (asteroids, drawable, updatable)

    AsteroidField.containers = updatable

    AsteroidField()

    Player(SCREEN_WIDTH / 2, SCREEN_HEIGHT / 2)

    # Game Loop
    while True:
        # listen for game exit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                return

        # update controls
        updatable.update(dt)

        # update visuals
        screen.fill(Color(0, 0, 0))
        for obj in drawable:
            obj.draw(screen)

        # End of Game Loop
        pygame.display.flip()
        dt = clock.tick(60) / 1000


if __name__ == "__main__":
    print("Starting Asteroids!")
    print(f"Screen width: {SCREEN_WIDTH}")
    print(f"Screen height: {SCREEN_HEIGHT}")
    main()
