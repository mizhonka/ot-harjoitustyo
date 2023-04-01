import pygame
import math
from level import Level

LEVEL_X=9
LEVEL_Y=9
MINE_X=10

def main():
    display=pygame.display.set_mode((LEVEL_X*50, LEVEL_Y*50))
    pygame.display.set_caption("Miinaharava")
    level=Level(LEVEL_X, LEVEL_Y, MINE_X)
    pygame.init()
    level.all_sprites.draw(display)
    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
            elif event.type==pygame.MOUSEBUTTONUP:
                pos=pygame.mouse.get_pos()
                y=int(math.modf(pos[0]/50)[1])
                x=int(math.modf(pos[1]/50)[1])
                
        pygame.display.update()
    pygame.quit()

if __name__=="__main__":
    main()