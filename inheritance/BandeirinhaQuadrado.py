from Bandeirinha import Bandeirinha

class BandeirinhaQuadrado(Bandeirinha):
    def __init__(self, px, py, ptamanho=None):
        super(BandeirinhaQuadrado, self).__init__(px, py, ptamanho)
        self.cor_quadrado = color(random(256),
                                  random(256),
                                  random(256)) 
                
    def desenha(self):
        super(BandeirinhaQuadrado, self).desenha()
        fill(self.cor_quadrado)
        rect(self.x - self.tamanho / 8,
             self.y - self.tamanho / 8,
             self.tamanho / 4,
             self.tamanho / 4)
        