import pygame
import random
import math
import PieceModule as pm

# Inicializa pygame y crea una ventana
pygame.init()
width, height = 800, 800
velMovement = 10
iconSize = 30
run = True
screen = pygame.display.set_mode((width, height))
SCISSORS = "scissors.png"
PAPER = "paper.png"
ROCK = "rock.png"
frameRate = 15

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('A bit Racey')

clock = pygame.time.Clock()
running = True

carImg = pygame.image.load('rock.png')
carImg = pygame.transform.scale(carImg, (iconSize, iconSize))

p1 = pm.Piece([random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],
 velMovement, iconSize, SCISSORS)
p2 = pm.Piece([random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],
 velMovement, iconSize, ROCK)
p3 = pm.Piece([random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],
 velMovement, iconSize, PAPER)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    p1.MovePiece(screen)
    p1.DrawPiece(screen)
    p2.MovePiece(screen)
    p2.DrawPiece(screen)
    p3.MovePiece(screen)
    p3.DrawPiece(screen)

    pygame.display.update()
    clock.tick(frameRate)

pygame.quit()
quit()