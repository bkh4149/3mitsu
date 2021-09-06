import pygame
from pygame.locals import QUIT,KEYDOWN,K_SPACE
import sys

def seen1(screen,font1,font2,level):
    ck = pygame.time.Clock()
    isSpacekey=False
    dict={1:30, 2:55, 3:103}
    sec=dict[level]

    while (1):
        screen.fill((255,255,255))# 画面を白に
        txt_pic = font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()
 
        txt = "Survive " + str(sec) + "sec !! "
        txt_pic = font1.render(txt, True, (150,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

        txt_pic = font2.render("then you can Level up! ", True, (100,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 300])# 文字列の表示位置        P1.update()

        txt_pic = font2.render("hit space key to start", True, (100,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 400])# 文字列の表示位置        P1.update()
        for event in pygame.event.get():
            if event. type == QUIT:
                pygame.quit()
                sys. exit()
            elif event.type == KEYDOWN:
                if event.key==K_SPACE:
                    isSpacekey=True
        if isSpacekey:
            break
        pygame.display.update() # 画面更新
        ck.tick(60) #1秒間で30フレームになるように33msecのwait
    return "s2"

