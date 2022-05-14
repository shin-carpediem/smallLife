import pygame
import math


def ngon(
      screen,
      color = (255, 255, 255),
      gx = 100,
      gy = 100,
      gr = 100,
      n = 5,
      rot = 0
  ):
  points = [
      (
          gr * math.cos(th) +
          gx, gr * math.sin(th) +
          gy
      )
      for th in
      [
          i * 2 * math.pi / n -
          math.pi / 2 +
          rot for i in range(n)
      ]
  ]
  pygame.draw.polygon(
      screen,
      color = color,
      points = points,
      width = 1
  )
