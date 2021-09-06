import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE
import seen1
import seen2
import seen3
import seen4


def main():
    pygame.init()
    font = pygame.font.Font(None, 100)
    font2 = pygame.font.Font(None, 50)
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面

    isSpacekey=False
    isQkey=False
    isWin=False
    level=3

    seen1.seen1(screen, font,font2,level)
    while True:
        isWin = seen2.seen2(screen, font2,level)
        if isWin:  #You Win
            level += 1
            (isSpacekey,isQkey)=seen3.seen3(screen, font,font2,level)
        else:      #Game over
            level -= 1
            (isSpacekey,isQkey)= seen4.seen4(screen, font,font2,level)
        if isQkey:
            break
    print("otu!")
    #======================
if __name__ == "__main__":
    main()

















