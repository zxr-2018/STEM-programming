import pygame
import random
import go #导入行驶模块
import time

x=400#图片的竖向位置
y=300#图片的横向位置
x_speed=25#图片的竖向移动速度
y_speed=25#图片的横向移动速度
clock=150#移动图片的等待时间
pygame.init()#初始化pygame
screen = pygame.display.set_mode([800,600])
screen.fill([255,255,255])
my_car = pygame.image.load("mycar.jpg")#加载图片
screen.blit(my_car,[x,y])#设置图片位置
pygame.display.flip()#刷新画面

running = True
while running == True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:#如果关闭窗口        
          running = False#条件为否，退出循环
          go.cleanup()#清空引脚
          
   r=random.randint(1,4)#设置随机数，上 下 左 右
      
   if r==1:
          go.run()#前进
          time.sleep(0.3)
          pygame.time.delay(clock)       
          pygame.draw.rect(screen,[255,255,255],[x,y,162,106],0)#遮盖移动痕迹    
          x=x+x_speed#调整位置
          screen.blit(my_car,[x,y])#绘制图片位置
          pygame.display.flip()#刷新画面
          go.stop()#停止移动小车
       
   elif r==2:
          go.back()#后退
          time.sleep(0.3)
          pygame.time.delay(clock)       
          pygame.draw.rect(screen,[255,255,255],[x,y,162,106],0)#遮盖移动痕迹
          x=x-x_speed#调整位置
          screen.blit(my_car,[x,y])#绘制图片位置
          pygame.display.flip()#刷新画面
          go.stop()#停止移动小车
       
   elif r==3:
          go.right()#右转
          time.sleep(0.3)
          pygame.time.delay(clock)       
          pygame.draw.rect(screen,[255,255,255],[x,y,162,106],0)
          y=y+y_speed#调整位置
          screen.blit(my_car,[x,y])#绘制图片位置
          pygame.display.flip()#刷新画面
          go.stop()#停止移动小车
   elif r==4:
          go.left()#左转
          time.sleep(0.3)
          pygame.time.delay(clock)       
          pygame.draw.rect(screen,[255,255,255],[x,y,162,106],0)
          y=y-y_speed#调整位置
          screen.blit(my_car,[x,y])#绘制图片位置
          pygame.display.flip()#刷新画面
          go.stop()#停止移动小车
      
pygame.quit()#关闭窗口
