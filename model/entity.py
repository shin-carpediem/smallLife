import random
import pygame
from constraint.constraint import HEIGHT, WIDTH
from func.draw import ngon


XMIN, XMAX = -1.5, 1.5
YMIN, YMAX = -1.5, 1.5


class Entity:
    def __init__(
        self,
        hue = 0,
        sat = 0,
        brightness = 1,
        radius = 0.1
      ):
      self.hue = hue # [0, 1]
      self.sat = sat # [0, 1]
      self.brightness = brightness # [0, 1]
      self._color = pygame.Color(0)
      self._updateColor()
      self.x = random.uniform(-1, 1)
      self.y = random.uniform(-1, 1)
      self.radius = radius
      self.alive = True


    def draw(
        self,
        screen,
        color,
        gx,
        gy,
        gr
      ):
      ngon(
          screen,
          color,
          gx,
          gy,
          gr,
          4
        )


    def _updateColor(self):
        self._color.hsva = 360 * self.hue, 100 * self.sat, 100 * self.brightness, 100


    def update(self, screen):
        if self.alive:
            self._updateColor()
            # Processing の map 関数が便利なので実装をコピー
            def map(
                value,
                istart,
                istop,
                ostart,
                ostop
              ):
                return ostart + (ostop - ostart) * ((value - istart) / (istop - istart))
            
            gx = map(
                self.x,
                XMIN,
                XMAX,
                0,
                WIDTH
              )
            gy = map(
                self.y,
                YMIN,
                YMAX,
                HEIGHT,
                0
              )
            gr = map(
                self.radius,
                0,
                XMAX,
                0,
                WIDTH / 2
              )
            self.draw(
                screen,
                self._color,
                gx,
                gy,
                gr
              )


    def collideWith(self, other) -> bool:
        dx = self.x - other.x
        dy = self.y - other.y
        rr = self.radius + other.radius
        return dx * dx + dy * dy < rr * rr
