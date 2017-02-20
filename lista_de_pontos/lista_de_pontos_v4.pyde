""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
"""
lista = []  # lista de pontos
TAM = 5   # tamanho dos círculos

def setup():
    size(600, 600)
    strokeWeight(2)
    stroke(255)   # traço/linha e branco
    fill(0)       # preenchinmento preto
    for _ in range(3):
        x, y, cor = random(width), random(height), cor_rnd(128)  # sorteia um ponto
        lista.append((x, y, cor))  # acrescenta uma tupla de um ponto na lista

def draw():
    background(0)             # limpa a tela
    for x1, y1, _ in lista:      # para cada ponto
        for x2, y2, cor in lista:  # pegue um segundo ponto (inclui o mesmo)
            if (x1, y1) != (x2, y2):
                stroke(cor)
                arrow(x1, y1, x2, y2)      # desenha linha
                fill(cor)
                ellipse(x2, y2, TAM, TAM)  # desenha círculo

def arrow(x1, y1, x2, y2):
    d = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x2, y2)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = -10
        line(0, offset, 0, -d - offset)
        line(0, offset, -10, -10 + offset)
        line(0, offset, 10, -10 + offset)
        
def cor_rnd(alpha_value=255):
    return color(random(255), random(255), random(255), alpha_value)

def mousePressed():                # clique do mouse
    lista.append((mouseX, mouseY, cor_rnd(128)))  # acrescenta ponto (tupla)

def keyPressed():               # tecla pressionada
    if len(lista) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = lista.pop(0)  # remove primeiro ponto (tupla)
        print(removido)
