import pygame
from pygame.locals import QUIT,KEYDOWN,K_SPACE,K_q
import sys

def seen4(screen,font1,font2,level,level_dict):
    ck = pygame.time.Clock()
    isSpacekey=False
    isQkey=False
    while (1):
        screen.fill((255,255,255))# 画面を白に
        txt_pic = font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()

        txt_pic = font1.render("oh no! ", True, (150,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

        txt_pic = font2.render("your Level down! "+str(level), True, (100,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 300])# 文字列の表示位置        P1.update()

        txt_pic = font2.render("hit space key to restart", True, (100,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 400])# 文字列の表示位置

        txt_pic = font2.render("hit q key to quit", True, (100,0,0))   # 描画する文字列の設定
        screen.blit(txt_pic, [100, 500])# 文字列の表示位置        P1.update()
        for event in pygame.event.get():
            if event. type == QUIT:
                pygame.quit()
                sys. exit()
            elif event.type == KEYDOWN:
                if event.key==K_SPACE:
                    isSpacekey=True
                elif event.key==K_q:
                    isQkey=True
        if isSpacekey or isQkey:
            break
        pygame.display.update() # 画面更新
        ck.tick(60) #1秒間で30フレームになるように33msecのwait
    return (isSpacekey,isQkey)