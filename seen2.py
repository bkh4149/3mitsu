import pygame
from pygame.locals import QUIT,KEYDOWN,K_LEFT,K_RIGHT,K_UP,K_DOWN,K_SPACE
import sys
import random
import time

class Judge():
    def __init__(self,sec):
        self.leftTime = sec
        self.countDownTime = 0
        self.gameStartTime = int(time.time())

    def update(self):
        nowTime = int(time.time())
        self.countDownTime = self.leftTime - (nowTime - self.gameStartTime)

    def draw(self,screen,font,P):
        txt = "HP="+str(P.hitpoint)
        txt_pic = font.render(txt, True, (100,0,0))
        screen.blit(txt_pic, [20, 50])

        txt = "Level "+str(P.level)
        txt_pic = font.render(txt, True, (100,0,0))
        screen.blit(txt_pic, [220, 50])

        txt = "CountDown "+str(self.countDownTime)+"sec"
        txt_pic = font.render(txt, True, (100,0,0))
        screen.blit(txt_pic, [20, 100])

class Player():
    def __init__(self, hp, level):
        self.x = 400
        self.y = 300
        self.r1 = 15
        self.vx = 0
        self.vy = 0
        self.hitpoint = hp
        self.red = 0
        self.blue = 250
        self.rate = self.blue/hp
        self.level = level
        self.isHit =False
        self.tc = 60
    def update(self):
        self.x += self.vx
        self.y += self.vy
        if self.x > 800:
            self.x -= 2.5
        elif self.x < 0:
            self.x += 2.5
        if self.y > 600:
            self.y -= 2.5
        elif self.y < 0:
            self.y += 2.5
        for event in pygame.event.get():
            if event. type == QUIT:
                pygame.quit()
                sys. exit()
            elif event.type == KEYDOWN:
                if event.key==K_LEFT:
                    self.vx = -1.3  # 横方向の速度
                elif event.key==K_RIGHT:
                    self.vx = 1.3  # 横方向の速度
                elif event.key==K_UP:
                    self.vy = -1.3
                elif event.key==K_DOWN:
                    self.vy = 1.3 
                elif event.key==K_SPACE:
                    self.tc = 10 
        if self.tc < 60:
            self.tc += 1
        return int(self.tc)
    def draw(self,screen):
        if self.r1 > 15:#衝突時爆発
            self.r1 -= 0.5
            pygame.draw.circle(screen,(255,0,0),(int(self.x),int(self.y)),int(self.r1))
        else:
            self.blue = self.hitpoint*self.rate
            self.red = 255 - self.blue
            pygame.draw.circle(screen,(int(self.red),0,int(self.blue)),(int(self.x),int(self.y)),int(self.r1))
class Ball():
    def __init__(self,x,y):
        self.x = x
        self.y = y
        self.vx = random.randint(10,30)/10
        self.vy = random.randint(8,32)/10
        self.col = (10,10,10)
        self.bc = 5
        self.r = 5
        self.isHit = False
        self.hitAnime = 0
    def update(self,P):
        self.x += self.vx
        self.y += self.vy
        if self.x >= 800 or self.x < 0:
            self.vx *= -1
        if self.y >= 600 or self.y < 0:
            self.vy *= -1
        #当たり判定
        if abs(self.x-P.x) <= (P.r1+self.r):
            if abs(self.y-P.y) <= (P.r1+self.r):
                if self.isHit:
                    pass
                else:
                    self.isHit = True
                    P.hitpoint -=1
                    P.isHit = True
                    P.r1= 30
                    self.r = 15
                #print(P.hitpoint)
        else:
            self.isHit=False
            P.isHit = False
    def draw(self,screen):
        if self.r>5:
            self.r-=0.1
            self.col = (210,110,10)
        else:    
            self.col = (10,10,10)
        pygame.draw.circle(screen,self.col,(int(self.x),int(self.y)),int(self.r))

def seen2(screen,font,level,level_dict):
    isWin=False
    ck = pygame.time.Clock()

    #審判
    sec=level_dict["sec"][level]
    J1=Judge(sec)
    #プレイヤ
    hp = level_dict["hp"][level]
    P1 = Player(hp, level)
    #敵
    teki = level_dict["teki"][level]
    Bs  = [Ball(random.randint(100,700), random.randint(100,500)) for i in range(teki)]
    tc = 60
    while (1):
        screen.fill((255,255,255))# 画面を白に
        tc = P1.update()
        P1.draw(screen)
        for i in range(teki):
            Bs[i].update(P1)
            Bs[i].draw(screen)
        J1.update()
        J1.draw(screen, font, P1)
        if P1.hitpoint < 2:
            isWin = False
            break
        if J1.countDownTime < 0:
            isWin = True
            break
        pygame.display.update() # 画面更新
        ck.tick(tc) #1秒間で30フレームになるように33msecのwait
    return isWin
