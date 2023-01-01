import pygame
import random
import math

# Inicializa pygame y crea una ventana
pygame.init()
width, height = 800, 800
velMovement = 20
radiusW = 20
run = True
screen = pygame.display.set_mode((width, height))

circle = [width//2,height//2]


while run:
    
    # Procesa eventos de pygame
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False
    
    # 0 = Up  1 = Rigth  2 = Down  3 = Left
    dir = math.floor(random.uniform(0,4))

    # if(dir == 0): #UP
    #     if((circle[1]-radiusW//2) > 0):
    #         circle[1] -= velMovement  
    # elif(dir == 1): #RIGTH
    #     if((circle[0]+radiusW//2) < width):
    #         circle[0] += velMovement 
    # elif(dir == 2): #DOWN
    #     if((circle[1]+radiusW//2) < height):
    #         circle[1] += velMovement  
    # elif(dir == 3): #LEFT
    #     if((circle[0]-radiusW//2) > 0):
    #         circle[0] -= velMovement 
        

    screen.fill((255, 255, 255))
    
    pygame.draw.circle(screen, (0, 0, 0), (int(circle[0]), int(circle[1])), radiusW)
    
    pygame.display.update()