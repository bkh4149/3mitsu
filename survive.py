import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE
# import sys
# import random
# import time
import seen1
import seen2
import seen3
import seen4


def main():
    pygame.init()
    font = pygame.font.Font(None, 100) # Pygameの初期化
    font2 = pygame.font.Font(None, 50) # Pygameの初期化
    screen = pygame.display.set_mode((800, 600))  # 800*600の画面
    isSpaceley=False
    isQkey=False

    seen1.seen1(screen, font,font2)
    while True:
        f = seen2.seen2(screen, font2)
        if f=="kachi":    
            #You Win
            (isSpaceley,isQkey)=seen3.seen3(screen, font,font2)
        else:    
            #Game over
            (isSpaceley,isQkey)= seen4.seen4(screen, font,font2)
        if isQkey:
            break
    #======================
if __name__ == "__main__":
    main()

















