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

    isSpacekey = False
    isQkey = False
    isWin = False

    level_dict = {"sec":{1:30, 2:55, 3:70, 4:90, 5:110}, "hp":{1:40, 2:75, 3:120, 4:160, 5:200}, "teki":{1:10, 2:20, 3:26, 4:32, 5:40}}
    level = 4

    seen1.seen1(screen, font, font2, level, level_dict)
    while True:
        isWin = seen2.seen2(screen, font2, level, level_dict)
        if isWin:  #You Win
            level += 1
            (isSpacekey, isQkey) = seen3.seen3(screen, font, font2, level, level_dict)
        else:      #Game over
            level -= 1
            (isSpacekey, isQkey)= seen4.seen4(screen, font, font2, level, level_dict)
        if isQkey:
            break
    print("otu!")
    #======================
if __name__ == "__main__":
    main()

















