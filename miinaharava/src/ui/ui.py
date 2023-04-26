import math
import pygame
from level import Level

LEVEL_X = 9
LEVEL_Y = 9
MINE_X = 10

def set_level(x, y, m):
    global LEVEL_X
    global LEVEL_Y
    global MINE_X
    LEVEL_X=x
    LEVEL_Y=y
    MINE_X=m

def mouse_pos():
    pos = pygame.mouse.get_pos()
    return (int(math.modf(pos[0]/50)[1]), int(math.modf(pos[1]/50)[1]))

def main():
    display = pygame.display.set_mode((LEVEL_X*50, LEVEL_Y*50))
    pygame.display.set_caption("Miinaharava")
    level = Level(LEVEL_X, LEVEL_Y, MINE_X)
    pygame.init()
    running = True
    first_click = True
    while running:
        for event in pygame.event.get():
            cords = mouse_pos()
            level.hover(cords[0], cords[1])
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 1:
                level.reveal(cords[0], cords[1], first_click)
                if first_click:
                    first_click = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button == 3:
                level.draw_flag(cords[0], cords[1])
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_ESCAPE:
                running = False
            elif event.type == pygame.KEYDOWN and event.key == pygame.K_r:
                level = Level(LEVEL_X, LEVEL_Y, MINE_X)
        level.init_sprites()
        level.all_sprites.draw(display)
        pygame.display.update()
    pygame.quit()

def difficulty():
    display = pygame.display.set_mode((250, 3*75))
    pygame.display.set_caption("Miinaharava")
    pygame.init()
    v=int(input("Vaikeus:"))
    if v==1:
        set_level(9, 9, 10)
    elif v==2:
        set_level(16,16,40)
    elif v==3:
        set_level(30, 16, 99)
    main()