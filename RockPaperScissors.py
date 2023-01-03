import pygame, random, math
import PieceModule as pm

print(pygame.__version__)

pygame.init()
width, height = 800, 800
VEL_MOVE = 10
ICON_SIZE = 50
NUM_PIECES = 30
FRAME_RATE = 10
screen = pygame.display.set_mode((width, height))

run = True
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

for i in range(NUM_PIECES):
    prob = math.floor(random.uniform(0,3))
    randomPos = [random.uniform(0, width - ICON_SIZE),random.uniform(0, height - ICON_SIZE)]
    pieza = None
    if(prob == 0):
        pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, SCISSORS, "scissors")
        pieza.add(scissorsGroup, allSpritesGroup)
    elif(prob == 1):
        pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, ROCK, "rock")
        pieza.add(rockGroup, allSpritesGroup)
    else:
        pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, PAPER, "paper")
        pieza.add(paperGroup, allSpritesGroup)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill((255,255,255))

    rockGroup.update(screen,rockGroup,paperGroup)
    scissorsGroup.update(screen,scissorsGroup,rockGroup)
    paperGroup.update(screen,paperGroup,scissorsGroup)

    allSpritesGroup.draw(screen)
    pygame.display.update()
    clock.tick(FRAME_RATE)

pygame.quit()