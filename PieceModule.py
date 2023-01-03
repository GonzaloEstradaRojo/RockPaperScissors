import pygame, random, math

class Piece(pygame.sprite.Sprite):
    
    collisions = None

    def __init__(self, pos, vel, iconSize, icon, group) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.icon = icon
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

    def MovePiece(self, screen):
        w, h = screen.get_size()
        seed = self.GenerateSeed()
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

    def update(self,screen, groupCollision, loserGroupCollision):
        self.MovePiece(screen)
        self.CheckCollisions(groupCollision, loserGroupCollision)
    