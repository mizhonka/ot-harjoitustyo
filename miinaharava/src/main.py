import math
import pygame
from level import Level

LEVEL_X = 9
LEVEL_Y = 9
MINE_X = 10

def mouse_pos():
    pos=pygame.mouse.get_pos()
    return (int(math.modf(pos[0]/50)[1]), int(math.modf(pos[1]/50)[1]))

def main():
    display = pygame.display.set_mode((LEVEL_X*50, LEVEL_Y*50))
    pygame.display.set_caption("Miinaharava")
    level = Level(LEVEL_X, LEVEL_Y, MINE_X)
    pygame.init()
    level.all_sprites.draw(display)
    running = True

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            elif event.type == pygame.MOUSEBUTTONUP and event.button==1:
                cords=mouse_pos()
                running = level.reveal(cords[0], cords[1])
            elif event.type == pygame.MOUSEBUTTONUP and event.button==3:
                cords=mouse_pos()
                level.draw_flag(cords[0], cords[1])
        level.all_sprites.draw(display)
        pygame.display.update()
    pygame.quit()


if __name__ == "__main__":
    main()
