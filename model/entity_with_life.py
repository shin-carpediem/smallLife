import random
import math
from .entity import Entity
from func.draw import ngon


class EntityWithLife(Entity):

    def __init__(self, hue=0, sat=0, life=100):
        self._life0 = life
        self._rot = random.uniform(0, 2 * math.pi)
        self.reset()
        super().__init__(hue=hue, sat=sat)

    def update(self, screen):
        if 0 < self.life:
            self.life -= 1
            self._age += 1
        else:
            self.life = 0
            self.alive = False

        self._rot += min(0.3, 0.005 * self.life)
        self.radius = min(0.1, 0.001 * self.life)

        super().update(screen)

    def draw(self, screen, color, gx, gy, gr):
        ngon(screen, color, gx, gy, gr, 3, self._rot)

    def reset(self):
        self.life = self._life0
        self.alive = True
        self._age = 0

    def isReproductive(self):
        return 30 < self._age and 10 < self.life
