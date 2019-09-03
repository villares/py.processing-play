""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
    Agora com uma classe Ponto!
"""
lista = []  # lista de pontos

def setup():
    size(600, 600)
    strokeWeight(2)
    stroke(0)     # traço/linha e branco
    fill(0)       # preenchinmento preto
    for _ in range(5):
        x, y, cor = random(width), random(height), cor_rnd()  # sorteia propriedades
        lista.append(Ponto(x, y, cor))  # acrescenta um ponto na lista

def draw():
    background(128)             # limpa a tela
    for ponto in lista:                  # para cada ponto
        for outro_ponto in lista:        # pegua um segundo ponto (inclui o mesmo)
            if ponto != outro_ponto:     # checa se não é o mesmo
                stroke(ponto.cor)
                desenha_seta(ponto.x, ponto.y, outro_ponto.x, outro_ponto.y) # desenha seta
                #fill(ponto.cor)
                ponto.desenha(10)
        
def cor_rnd(alpha_value=128):
    return color(random(128,255), random(128,255), random(128,255), alpha_value)

def mousePressed():                                 # clique do mouse
    lista.append(Ponto(mouseX, mouseY, cor_rnd()))  # acrescenta ponto na pos. clicada

def keyPressed():               # tecla pressionada
    if len(lista) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = lista.pop(0) # remove primeiro ponto da lista
                
def desenha_seta (x1, y1, x2, y2):
    d = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x2, y2)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = -20 
        head = 6
        line(0, offset, 0, -d - offset)
        line(0, offset, -head/3, -head + offset)
        line(0, offset, head/3, -head + offset)

class Ponto:
    def __init__(self, x, y, cor = color(0)):
        self.x = x
        self.y = y
        self.cor = cor
    def desenha(self, tamanho):
        ellipse(self.x, self.y, tamanho, tamanho)
 
    
