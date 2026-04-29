import random
import pygame
from circleshape import CircleShape
from constants import LINE_WIDTH, ASTEROID_MIN_RADIUS
from logger import log_event


class Asteroid(CircleShape):
    def __init__(self, x, y, radius):
        super().__init__(x, y, radius)

    def draw(self, screen):
        pygame.draw.circle(screen, "white", self.position, self.radius, LINE_WIDTH)

    def update(self, delta_time):
        self.position += self.velocity * delta_time

    def split(self):
        self.kill()

        if self.radius <= ASTEROID_MIN_RADIUS:
            return

        log_event("asteroid_split")
        random_angle = random.uniform(20, 50)

        first_child_velocity = self.velocity.rotate(random_angle)
        second_child_velocity = self.velocity.rotate(-random_angle)

        child_radius = self.radius - ASTEROID_MIN_RADIUS
        child1 = Asteroid(self.position.x, self.position.y, child_radius)
        child2 = Asteroid(self.position.x, self.position.y, child_radius)

        child1.velocity = first_child_velocity * 1.2
        child2.velocity = second_child_velocity * 1.2
