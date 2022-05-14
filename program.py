import pygame
from constraint.constraint import FPS
from func.screen import quit, clear, update
from model.entity import WIDTH, HEIGHT
from model.entity_with_life import EntityWithLife


# 画面を初期化
pygame.init()

entities = [EntityWithLife() for _ in range(10)]
screen = pygame.display.set_mode((WIDTH, HEIGHT))

while not quit():
    clear(screen)

    for e in entities:
        e.update(screen)

    entities = [x for x in entities if x.alive]
    update(FPS)

pygame.display.quit()
