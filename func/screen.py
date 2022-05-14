import pygame


# プログラムを停止させることを選んだかどうかの判定
def quit():
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.event.clear()
            return True
    return False


# 画面の消去
def clear(screen):
    screen.fill((100, 100, 100))


# 画面の更新
def update(fps):
    pygame.display.update()
    pygame.time.Clock().tick(fps)
