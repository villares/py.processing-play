"""
Prova de conceito para mapa em 3D (câmera cotrolada pelo mouse)
"""

import random as rnd

TAMANHO = 50  # tamanho grade
MAPA = []

def setup():
    global MAPA, COLUNAS, FILAS
    size(600, 600, P3D)
    COLUNAS = width / TAMANHO
    FILAS = height / TAMANHO
    for fila in range(FILAS):
        for coluna in range(COLUNAS):
            tipo = rnd.choice(Quadrado.TIPOS)
            altura = sorteiaAltura(tipo)
            quadrado = Quadrado(fila, coluna, tipo, altura)
            MAPA.append(quadrado)

def draw():
    '''for quadrado in MAPA:
            quadrado.desenha()
    '''
    background(0)
    camera(mouseX, mouseY*2, 500.0,  # eyeX, eyeY, eyeZ
           width/2,height/2, 0.0,        # centerX, centerY, centerZ
           0.0, 1.0, 0.0)        # upX, upY, upZ
    for fila in range(FILAS):
        for coluna in range(COLUNAS):
            quadrado = no_mapa(fila, coluna)
            quadrado.desenha()

class Quadrado():
    ''' Região quadrada do mapa'''
    
    AMARELO = color(255, 230, 0)
    AZUL_ESCURO = color(7, 0, 255)
    MARROM_ESCURO = color(85, 25, 27)
    VERDE_CLARO = color(10, 237, 7)
    MARROM_CLARO = color(193, 109, 111)
    VERDE_ESCURO = color(48, 72, 36)
    TIPOS = ["mar", "montanha", "praia", "plano", "vila", "floresta"]
    CORES = {"mar": AZUL_ESCURO,
             "montanha": MARROM_ESCURO,
             "praia": AMARELO,
             "plano": VERDE_CLARO,
             "vila": MARROM_CLARO,
             "floresta": VERDE_ESCURO}

    def __init__(self, fila, coluna, tipo, altura):
        self.fila = fila
        self.coluna = coluna
        self.tipo = tipo
        self.altura = altura
        self.cor = Quadrado.CORES[tipo]


    def desenha(self):
        posX, posY = self.coluna * TAMANHO, self.fila * TAMANHO
        with pushMatrix():
            translate(posX, posY)
            noStroke()
            fill(self.cor)
            pushMatrix()
            translate(0,0,self.altura)
            rect(0, 0, TAMANHO, TAMANHO)
            popMatrix()
            fill(255)       # branco
            textSize(10)  # para escrever o tipo se o mouse estiver perto
            if (dist(posX, posY, mouseX, mouseY) < TAMANHO * 2):
                text(self.tipo, 0, 20, self.altura+5)
                
def no_mapa(fila, coluna):
        return MAPA[coluna + fila * COLUNAS]
    
def sorteiaAltura(tipo):
    #return 0 #(para demo plana)
    if tipo == "mar" or tipo == "praia":
        return 0
    elif tipo == "montanha":
        return 30
    else:
        return random (5,25)

    
    
