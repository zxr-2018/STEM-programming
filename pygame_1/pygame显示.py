import pygame

pygame.init()
screen = pygame.display.set_mode([400,400])
screen.fill([255,255,255])
my_car = pygame.image.load("mycar.jpg")
screen.blit(my_car , [119,147])
pygame.display.flip()


running = True
while running == True:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         running = False
pygame.quit()
