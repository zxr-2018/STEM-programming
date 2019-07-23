import pygame
import random
import go
import time 

def a():
    pygame.init()
    screen = pygame.display.set_mode([200,50])
    running = True
    while running == True:
       for event in pygame.event.get():
          if event.key == pygame.K_e:          
              running = False            
       r=random.randint(1,4)
      
       if r==1:
          go.run()
          time.sleep(0.3)
          go.stop()
       
       elif r==2:
          go.back()
          time.sleep(0.3)
          go.stop()
       
       elif r==3:
          go.right()
          time.sleep(0.3)
          go.stop()
          
       elif r==4:
          go.left()
          time.sleep(0.3)
          go.stop()
      
pygame.quit()
