import pygame
from pygame.locals import *
from time import *
pygame .init()

WIDTH = 600
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH,HEIGHT))
p_x = 200 
p_y = 200

#keys = [False,False,False,False]
p = pygame.image.load('r.png')
s = pygame.image.load('s.png')

# while p_y < 600:
#     screen.blit(s,(0,0))
#     screen.blit(p,(p_x,p_y))
#     pygame.display.flip()
while True:
    screen.blit(s,(0,0)) 
    screen.blit(p,(p_x,p_y))
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w and p_y > 0:
                p_y -= 20
                pygame.display.update()

            if event.key == pygame.K_s and p_y < 400:
                p_y += 20
                pygame.display.update()

            if event.key == pygame.K_a and p_x > 0:
                p_x -= 20
                pygame.display.update()

            if event.key == pygame.K_d and p_x < 450:
                p_x += 20
                pygame.display.update()
                            
    pygame.display.update()
