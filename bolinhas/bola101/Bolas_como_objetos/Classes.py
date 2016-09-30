
class Bola():
    def __init__(self,px,py, v, cor):
        self.x = px
        self.y = py
        self.cor = cor
        self.velocidade_x = v
        self.velocidade_y = v
    
    def mostra(self):
        fill(self.cor)
        ellipse(self.x, self.y, 10,10)

    def anda(self):
        self.x += self.velocidade_x # self.x = self.x + self.velocidade_x
        self.y += self.velocidade_y
        if not(0 < self.x < width):
            self.velocidade_x = -self.velocidade_x
        if not(0 < self.y < height):
            self.velocidade_y = -self.velocidade_y