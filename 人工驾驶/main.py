import pygame
import autodrive
import humandrive

screen=pygame.display.set_mode([100,100])

def main():
   while True:   
      for event in pygame.event.get():
         if event.type == pygame.KEYDOWN:
           if event.key == pygame.K_a:
              autodrive.a()

           if event.key == pygame.K_h:
               humandrive.h()
main() 
