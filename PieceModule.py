import pygame
import random
import math

# class Piece:
#     def __init__(self, name, pos, vel, iconSize, icon) -> None:
#         self._pos = pos
#         self._posX = pos[0]
#         self._posY = pos[1]
#         self._vel = vel
#         self._iconSize = iconSize
#         self._icon = icon
#         self._image = pygame.transform.scale(pygame.image.load(icon), (iconSize, iconSize))
#         self._rect = self._image.get_rect()
#         self._name = name

#     def GenerateSeed(self):
#         return math.floor(random.uniform(0,4))   

#     def MovePiece(self, screen):
#         w, h = screen.get_size()
#         seed = self.GenerateSeed()
#         if(seed == 0): #LEFT
#             if((self._posX) > 0):
#                 self._posX -= self._vel 
#         elif(seed == 1): #RIGTH
#             if((self._posX + self._iconSize) <= w):
#                 self._posX += self._vel  
#         elif(seed == 2): #UP
#             if((self._posY) > 0):
#                 self._posY -= self._vel   
#         elif(seed == 3): #DOWN
#             if((self._posY + self._iconSize) < h):
#                 self._posY += self._vel   
    
#     def DrawPiece(self, screen):
#         image = pygame.image.load(self._icon)
#         rectangle = pygame.Rect(self._posX, self._posY, self._iconSize, self._iconSize)

#         pygame.draw.rect(screen, (0,0,0), rectangle)
#         screen.blit(self._image, (self._posX, self._posY))

#     def CheckCollision(self, collisionList):
#         # print("type ", type(self._rect))
#         # print(dir(self._rect))
#         # result = self._rect.collideobjects(collisionList)
#         # print(f"La pieza {self._name} se ha chocado con {result._name}")
#         pass

#     def ChangeIcon(self):
#         pass

class Piece(pygame.sprite.Sprite):
    def __init__(self, name, pos, vel, iconSize, icon) -> None:
        pygame.sprite.Sprite.__init__(self)
        self.image = pygame.transform.scale(pygame.image.load(icon), (iconSize, iconSize))
        self.rect = self.image.get_rect()
        self.rect.x = pos[0]
        self.rect.y = pos[1]
        self.vel = vel

        self.pos = pos
        self.posX = pos[0]
        self.posY = pos[1]
        self.icon = icon
        self.iconSize = iconSize
        self.name = name

    def GenerateSeed(self):
        return math.floor(random.uniform(0,4))   

    def update(self, screen):
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
        elif(seed == 3): #DOWN
            if((self.rect.y + self.iconSize) < h):
                self.rect.y += self.vel   
    