import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE,K_q
import seen2
import sys
class Game():
    def __init__(self):
        self.font1 = pygame.font.Font(None, 100)
        self.font2 = pygame.font.Font(None, 50)
        self.screen = pygame.display.set_mode((800, 600))  # 800*600の画面
        self.isSpacekey = False
        self.isQkey = False
        self.isWin = False
        self.level_dict = {"sec":{1:10, 2:15, 3:20, 4:20, 5:20}, "hp":{1:40, 2:75, 3:120, 4:160, 5:200}, "teki":{1:10, 2:20, 3:26, 4:32, 5:40}}
        #self.level_dict = {"sec":{1:30, 2:55, 3:70, 4:90, 5:110}, "hp":{1:40, 2:75, 3:120, 4:160, 5:200}, "teki":{1:10, 2:20, 3:26, 4:32, 5:40}}
        self.level = 1

    def seen1(self):
        ck = pygame.time.Clock()
        self.isSpacekey=False
        self.sec=self.level_dict["sec"][self.level]

        while (1):
            self.screen.fill((255,255,255))# 画面を白に
            txt_pic = self.font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()
    
            txt = "Survive " + str(self.sec) + "sec !! "
            txt_pic = self.font1.render(txt, True, (150,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("then you can Level up! ", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 300])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("hit space key to start", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 400])# 文字列の表示位置        P1.update()
            for event in pygame.event.get():
                if event. type == QUIT:
                    pygame.quit()
                    sys.exit()
                elif event.type == KEYDOWN:
                    if event.key==K_SPACE:
                        self.isSpacekey=True
            if self.isSpacekey:
                break
            pygame.display.update() # 画面更新
            ck.tick(60) #1秒間で30フレームになるように33msecのwait

    def seen3(self):
        ck = pygame.time.Clock()
        self.isSpacekey=False
        self.isQkey=False
        while (1):
            self.screen.fill((255,255,255))# 画面を白に
            txt_pic = self.font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()

            txt_pic = self.font1.render("Congratulation!! ", True, (150,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

            txt = "now, your Level is up to " + str(self.level)
            txt_pic = self.font2.render(txt, True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 300])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("hit space key to start", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 400])# 文字列の表示位置
            
            txt_pic = self.font2.render("hit q key to quit", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 500])# 文字列の表示位置        P1.update()
            for event in pygame.event.get():
                if event. type == QUIT:
                    pygame.quit()
                    sys. exit()
                elif event.type == KEYDOWN:
                    if event.key==K_SPACE:
                        self.isSpacekey=True
                    elif event.key==K_q:
                        self.isQkey=True
            if self.isSpacekey or self.isQkey:
                break
            pygame.display.update() # 画面更新
            ck.tick(60) #1秒間で30フレームになるように33msecのwait

    def seen4(self):
        ck = pygame.time.Clock()
        self.isSpacekey=False
        self.isQkey=False
        while (1):
            self.screen.fill((255,255,255))# 画面を白に
            txt_pic = self.font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()

            txt_pic = self.font1.render("oh no! ", True, (150,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("your Level down! "+str(level), True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 300])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("hit space key to restart", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 400])# 文字列の表示位置

            txt_pic = self.font2.render("hit q key to quit", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 500])# 文字列の表示位置        P1.update()
            for event in pygame.event.get():
                if event. type == QUIT:
                    pygame.quit()
                    sys. exit()
                elif event.type == KEYDOWN:
                    if event.key==K_SPACE:
                        self.isSpacekey=True
                    elif event.key==K_q:
                        self.isQkey=True
            if self.isSpacekey or self.isQkey:
                break
            pygame.display.update() # 画面更新
            ck.tick(60) #1秒間で30フレームになるように33msecのwait

    #最終勝利
    def seen5(self):
        ck = pygame.time.Clock()
        self.isSpacekey=False
        self.isQkey=False
        while (1):
            self.screen.fill((255,255,255))# 画面を白に
            txt_pic = self.font2.render("Survive Game", True, (200,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 100])# 文字列の表示位置        P1.update()

            txt_pic = self.font1.render("Awesome!!!! ", True, (150,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 200])# 文字列の表示位置        P1.update()

            txt_pic = self.font2.render("hit q key to quit", True, (100,0,0))   # 描画する文字列の設定
            self.screen.blit(txt_pic, [100, 500])# 文字列の表示位置        P1.update()

            for event in pygame.event.get():
                if event. type == QUIT:
                    pygame.quit()
                    sys. exit()
                elif event.type == KEYDOWN:
                    if event.key==K_q:
                        self.isQkey=True
            if self.isSpacekey or self.isQkey:
                break
            pygame.display.update() # 画面更新
            ck.tick(60) #1秒間で30フレームになるように33msecのwait


    def main(self):
        self.seen1()
        #seen1.seen1(self.screen, self.font, self.font2, self.level, self.level_dict)
        while True:
            self.isWin = seen2.seen2(self.screen, self.font2, self.level, self.level_dict)
            if self.isWin:  #You Win
                if self.level == 5:
                    self.seen5()
                else:
                    self.level += 1
                    self.seen3()
            else:      #Game over
                self.level -= 1
                self.seen4()
            if self.isQkey:
                break
        print("Otukaresama deshita!")


def main():
    pygame.init()
    G1=Game()
    G1.main()

if __name__ == "__main__":
    main()

