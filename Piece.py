class Pieza:
    def __init__(self, pos, vel, radius, value) -> None:
        self._posX = pos[0]
        self._posY = pos[1]
        self._vel = vel
        self.radius = radius
        self._value = value

    def MovePiece(self, seed, bounds):
        
        if(seed == 0): #UP
            if((self._posY - self.radius//2) > 0):
                self._posY -= self._vel   
        elif(seed == 1): #RIGTH
            if((self._posX + self.radius//2) < bounds[0]):
                self._posX += self._vel  
        elif(seed == 2): #DOWN
            if((self._posY + self.radius//2) < bounds[1]):
                self._posY += self._vel   
        elif(seed == 3): #LEFT
            if((self._posX - self.radius//2) > 0):
                self._posX -= self._vel 
            