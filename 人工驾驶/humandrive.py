import go
import pygame
import time

def h():
   pygame.init()
   pygame.key.set_repeat(150,0)
   screen=pygame.display.set_mode([320,280])
   running=True
   while running==True:
      for event in pygame.event.get():
         if event.key ==pygame.K_e:         
            running==False
         if event.key ==pygame.K_w:
            go.run()
            time.sleep(0.3)
            go.stop()

         if event.key ==pygame.K_a:
            go.left()
            time.sleep(0.3)
            go.stop()

         if event.key ==pygame.K_s:
            go.back()
            time.sleep(0.3)
            go.stop()

         if event.key ==pygame.K_d:
            go.right()
            time.sleep(0.3)
            go.stop()

         
pygame.quit()
