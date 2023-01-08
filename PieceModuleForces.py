import pygame, random, math

class Piece(pygame.sprite.Sprite):
    
    collisions = None

    def __init__(self, pos, vel, iconSize, icon, group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.icon = icon
        self.pos = pos
        self.iconSize = iconSize
        self.image = pygame.transform.scale(pygame.image.load(self.icon), (self.iconSize, self.iconSize))
        self.rect = self.image.get_rect()
        self.rect.x, self.rect.y = pos
        self.vel = vel
        self.group = group
        self.GetRelations(self.group)
      
    def GetRelations(self, group):
        if(group == "scissors"):
            self.defeatedBy = "rock"
            self.winTo = "paper"
        elif(group == "paper"):
            self.defeatedBy = "scissors"
            self.winTo = "rock"
        elif(group == "rock"):
            self.defeatedBy = "paper"
            self.winTo = "scissors"

    def GenerateSeed(self):
        return math.floor(random.uniform(0,4))   

    def MovePiece(self, screen, winnerGroup):
        w, h = screen.get_size()
        seed = self.GetDirectionWithMoreWinToPieces(winnerGroup)
        if(seed == 0): #LEFT
            if((self.rect.x) > 0):
                self.rect.x -= self.vel 
        elif(seed == 1): #RIGTH
            if((self.rect.x + self.iconSize) <= w):
                self.rect.x += self.vel  
        elif(seed == 2): #UP
            if((self.rect.y) > 0):
                self.rect.y -= self.vel   
        else: #DOWN
            if((self.rect.y + self.iconSize) < h):
                self.rect.y += self.vel   

    def CheckCollisions(self, selfGroupCollision, loserGroupCollision ):
        global collisions
        collisions = pygame.sprite.groupcollide(selfGroupCollision, loserGroupCollision, False, False)
        if collisions:
            for p in collisions:
                p.ChangePiece(selfGroupCollision, loserGroupCollision)

    def ChangePiece(self, selfGroupCollision, loserGroupCollision):
        self.group = self.defeatedBy
        self.icon = f"icons/{self.defeatedBy}.png"
        self.image = pygame.transform.scale(pygame.image.load(self.icon), (self.iconSize, self.iconSize))

        self.GetRelations(self.group)
        loserGroupCollision.add(self)
        selfGroupCollision.remove(self)

    def GetDirectionWithMoreWinToPieces(self, winGroup):
        print("Icono: ", self.icon)
        list_Positions_Higher = [1 for elem in winGroup if elem.rect.y <= self.rect.y]
        list_Positions_Lower = [1 for elem in winGroup if elem.rect.y >= self.rect.y]
        list_Positions_Rigther = [1 for elem in winGroup if elem.rect.x <= self.rect.x]
        list_Positions_Lefter = [1 for elem in winGroup if elem.rect.x >= self.rect.x]
        print(list_Positions_Higher, list_Positions_Lower, list_Positions_Rigther, list_Positions_Lefter)
        print("sum: ", sum(list_Positions_Higher), sum(list_Positions_Lower), sum(list_Positions_Rigther), sum(list_Positions_Lefter))
        
        direction = None
        maxSprites = max(sum(list_Positions_Higher), sum(list_Positions_Lower), sum(list_Positions_Rigther), sum(list_Positions_Lefter))
        if maxSprites == 0:
            direction = self.GenerateSeed()
        elif sum(list_Positions_Rigther) == maxSprites:
            direction = 0
        elif sum(list_Positions_Lefter) == maxSprites:
            direction = 1
        elif sum(list_Positions_Higher) == maxSprites:
            direction = 2
        elif sum(list_Positions_Lower) == maxSprites:
            direction = 3

        return direction
        # for elem in winGroup:
        #     print(elem.rect.x, elem.rect.y)
        # pass

    def GetDirectionWithMoreDefeatedByPieces(self, defeatedGroup ):
        pass

    def update(self,screen, selfGroup, loserGroup, winnerGroup):
        self.MovePiece(screen, winnerGroup)
        self.CheckCollisions(selfGroup, loserGroup)
    