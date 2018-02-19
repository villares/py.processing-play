""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
"""
lista = [] # lista de pontos
TAM = 10   # tamanho dos círculos

def setup():
    # fullScreen()
    size(600, 800)
    stroke(255)   # traço/linha e branco
    fill(0)       # preenchinmento preto
    for _ in range(10):                       
        x, y = random(width), random(height)  # sorteia um ponto
        lista.append((x,y)) # acrescenta uma tupla de um ponto na lista
    
def draw():
    background(0)             # limpa a tela
    for x1, y1 in lista:      # para cada ponto 
        for x2, y2 in lista:  # pegue um segundo ponto (inclui o mesmo)
            line (x1, y1, x2, y2)      # desenha linha
            ellipse(x2, y2, TAM, TAM)  # desenha círculo
        
def mousePressed():                # clique do mouse
    lista.append((mouseX,mouseY))  # acrescenta ponto (tupla)

def keyPressed():               # tecla pressionada
    if len(lista) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = lista.pop(0) # remove primeiro ponto (tupla)
        print(removido)
