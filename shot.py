import pygame
from circleshape import CircleShape
from constants import PLAYER_SHOOT_SPEED, SHOT_RADIUS


class Shot(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, SHOT_RADIUS, 0)

    def update(self, dt):
        self.position += dt * self.velocity
