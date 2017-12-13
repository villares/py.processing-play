from BandeirinhaQuadrado import BandeirinhaQuadrado 
from BandeirinhaCirculo import BandeirinhaCirculo

def Fabrica(px, py, ptamanho=None):
    if random(100) > 50:
        return BandeirinhaQuadrado(px, py, ptamanho)
    else:
        return BandeirinhaCirculo(px, py, ptamanho)