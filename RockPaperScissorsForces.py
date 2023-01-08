import pygame, random, math
import PieceModuleForces as pm

print(pygame.__version__)

pygame.init()
width, height = 800, 800
fontsizeGameOver = width//15
fontsizeText = width//(3*10)
VEL_MOVE = 30
ICON_SIZE = 50
NUM_PIECES = 60
FRAME_RATE = 10
screen = pygame.display.set_mode((width, height))

run = True
gameOver = False
winner = None
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

def CreaetNewPieces():
    for i in range(NUM_PIECES):
        prob = math.floor(random.uniform(0,3))
        randomPos = [random.uniform(0, width - ICON_SIZE),random.uniform(0, height - ICON_SIZE)]
        pieza = None
        if(prob == 0):
            pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, SCISSORS, "scissors")
            pieza.add(scissorsGroup)
        elif(prob == 1):
            pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, ROCK, "rock")
            pieza.add(rockGroup)
        else:
            pieza = pm.Piece(randomPos,VEL_MOVE, ICON_SIZE, PAPER, "paper")
            pieza.add(paperGroup)

def ResetPieces():
    scissorsGroup.empty()
    rockGroup.empty()
    paperGroup.empty()

def CheckGameOver():
    global gameOver, scissorsGroup, rockGroup, paperGroup, winner
    if(len(scissorsGroup) == NUM_PIECES):
        gameOver = True
        winner = "Scissors"
    elif(len(rockGroup) == NUM_PIECES):
        gameOver = True
        winner = "Rock"
    elif(len(paperGroup) == NUM_PIECES):
        gameOver = True
        winner = "Paper"

def DrawEndGame():
    
    fontGameOver = pygame.font.Font(None, fontsizeGameOver)
    fontText = pygame.font.Font(None, fontsizeText)
    screen_rect= screen.get_rect()

    rectTexto = pygame.Rect(0,0,width*0.5,height*0.5)
    rectBorde = pygame.Rect(0,0,width*0.5+10,height*0.5+10)
    rectTexto.center, rectBorde.center = screen_rect.center, screen_rect.center
    pygame.draw.rect(screen, (255,0,0), rectBorde)
    pygame.draw.rect(screen, (0,0,0), rectTexto)

    textGameOver = fontGameOver.render("GAME OVER", True, (255,255,255))
    textGameOver_rect = textGameOver.get_rect()
    textGameOver_rect.center = screen_rect.center
    textGameOver_rect.centery -= width*0.1
    
    textWinner = fontText.render(f"{winner.upper()} WINS!!", True, (255,255,255))
    textWinner_rect = textWinner.get_rect()
    textWinner_rect.center = screen_rect.center

    textInstructions = fontText.render("Press SPACE or CLICK to restart", True, (255,255,255))
    textInstructions_rect = textInstructions.get_rect()
    textInstructions_rect.center = screen_rect.center
    textInstructions_rect.centery += width*0.1
    
    screen.blit(textGameOver, textGameOver_rect)
    screen.blit(textWinner, textWinner_rect)
    screen.blit(textInstructions, textInstructions_rect)
    

def GameLoop():
    global running, gameOver
    ResetPieces()
    CreaetNewPieces()
    while running:
        events = pygame.event.get()
        for event in events:
            if event.type == pygame.QUIT:
                running = False
            if pygame.key.get_pressed()[pygame.K_r]:
                GameLoop()
        if not gameOver:    
            CheckGameOver()
            screen.fill((255,255,255))
            


            rockGroup.update(screen,rockGroup,paperGroup, scissorsGroup)
            scissorsGroup.update(screen,scissorsGroup,rockGroup, paperGroup)
            paperGroup.update(screen,paperGroup,scissorsGroup, rockGroup)
            
            rockGroup.draw(screen)
            scissorsGroup.draw(screen)
            paperGroup.draw(screen)
        else:
            DrawEndGame()
            for event in events:
                if ((pygame.key.get_pressed()[pygame.K_SPACE]) 
                or (event.type == pygame.MOUSEBUTTONUP and event.button == 1)):
                    running = True
                    gameOver = False
                    GameLoop()

        pygame.display.update()
        clock.tick(FRAME_RATE)

    pygame.quit()

if __name__ == "__main__":
    GameLoop()