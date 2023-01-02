import pygame
import random
import math
import PieceModule as pm

print(pygame.__version__)
# Inicializa pygame y crea una ventana
pygame.init()
width, height = 800, 800
velMovement = 15
iconSize = 30
numPieces = 30
frameRate = 10
run = True
screen = pygame.display.set_mode((width, height))
SCISSORS = "icons/scissors.png"
PAPER = "icons/paper.png"
ROCK = "icons/rock.png"

pygame.init()

screen = pygame.display.set_mode((width,height))
pygame.display.set_caption('Rock Paper Scissor')

clock = pygame.time.Clock()
running = True

scissorsGroup = pygame.sprite.Group(())
rockGroup = pygame.sprite.Group(())
paperGroup = pygame.sprite.Group(())
allSpritesGroup = pygame.sprite.Group(())

for i in range(numPieces):
    prob = math.floor(random.uniform(0,3))
    pieza = None
    if(prob == 0):
        pieza = pm.Piece(f"S{i}",[random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],velMovement, iconSize, SCISSORS)
        pieza.add(scissorsGroup,allSpritesGroup)
    elif(prob == 1):
        pieza = pm.Piece(f"R{i}",[random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],velMovement, iconSize, ROCK)
        pieza.add(rockGroup,allSpritesGroup)
    elif(prob == 2):
        pieza = pm.Piece(f"P{i}",[random.uniform(0, width-iconSize),random.uniform(0, height-iconSize)],velMovement, iconSize, PAPER)
        pieza.add(paperGroup,allSpritesGroup)

# pieceList = []
# pieceList.append(p1)
# pieceList.append(p2)
# pieceList.append(p3)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))
    allSpritesGroup.update(screen)
    # p1.MovePiece(screen)
    # p2.MovePiece(screen)
    # p3.MovePiece(screen)

    allSpritesGroup.draw(screen)
    # p1.DrawPiece(screen)
    # p2.DrawPiece(screen)
    # p3.DrawPiece(screen)

    # p1.CheckCollision(pieceList)
    # p2.CheckCollision(pieceList)
    # p3.CheckCollision(pieceList)

    pygame.display.update()
    clock.tick(frameRate)
pygame.quit()
quit()