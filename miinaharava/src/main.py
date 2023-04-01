import pygame
from level import Level

LEVEL_X=9
LEVEL_Y=9

def main():
    display=pygame.display.set_mode((LEVEL_X*50, LEVEL_Y*50))
    pygame.display.set_caption("Miinaharava")
    level=Level(LEVEL_X, LEVEL_Y, 10)
    pygame.init()
    level.all_sprites.draw(display)
    running=True

    while running:
        for event in pygame.event.get():
            if event.type==pygame.QUIT:
                running=False
        pygame.display.update()
    pygame.quit()

if __name__=="__main__":
    main()