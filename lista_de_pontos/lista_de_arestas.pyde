""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
    Para rodar, instale o Processing Modo Python.
"""
lista_pontos = []  # lista de pontos
lista_arestas = []

tamanho = 30 # tamanho dos 'pontos'
velocidade = 0.2 
pontos_iniciais = 5

def setup():
    size(600, 600)
    strokeWeight(2)
    stroke(255)     # traço/linha e branco
    noFill()       # sem preenchinmento
    for _ in range(pontos_iniciais):
        x, y = random(width), random(height)
        cor = cor_rnd() # sorteia cor
        lista_pontos.append(Ponto(x, y, cor))  # acrescenta um ponto na lista
    for i, ponto in enumerate(lista_pontos):
        for outro_ponto in lista_pontos[i:]:
            if ponto != outro_ponto:  # checa se não é o mesmo
                nova_aresta = Aresta(ponto, outro_ponto)
                lista_arestas.append(nova_aresta)

def draw():
    background(128)             # limpa a tela
    for ponto in lista_pontos:  # para cada ponto
        ponto.desenha()
        ponto.move()
    for aresta in lista_arestas:
        if (aresta.p1 not in lista_pontos) or (aresta.p2 not in lista_pontos):
            lista_arestas.remove(aresta)
            print(aresta.p1, aresta.p2)
        else:
            aresta.desenha_linha()

def cor_rnd(alpha_value=128):
    return color(random(128, 255), random(128, 255), random(128, 255), alpha_value)

def mouseClicked():  # ao soltar do mouse
    novo_ponto = Ponto(mouseX, mouseY, cor_rnd())
    for ponto in lista_pontos:
        nova_aresta = Aresta(ponto, novo_ponto)
        lista_arestas.append(nova_aresta)
    lista_pontos.append(novo_ponto)  # acrescenta poneto na pos. clicada

def keyPressed():               # tecla pressionada
    if len(lista_pontos) > 1:          # se a lista tiver pelo menos 2 pontos
        removido = lista_pontos.pop(0)  # remove primeiro ponto da lista

def mouseDragged():
    for ponto in lista_pontos:                  # para cada ponto
        if dist(mouseX, mouseY, ponto.x, ponto.y) < tamanho * 3 / 2:
            ponto.x, ponto.y = mouseX, mouseY

class Ponto():
    " pontos num grafo "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.cor = cor
        self.vx = random(-velocidade, velocidade)
        self.vy = random(-velocidade, velocidade)

    def desenha(self):
        fill(self.cor)
        ellipse(self.x, self.y, tamanho, tamanho)
        if dist(mouseX, mouseY, self.x, self.y) < tamanho * 3 / 2:
            stroke(0)
            noFill()
            ellipse(self.x, self.y, tamanho * 3, tamanho * 3)
            fill(0)
            text(str(len(lista_pontos))+" "+str(len(lista_arestas)), self.x, self.y)
        stroke(255)

    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy

class Aresta():

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2

    def desenha_linha(self):
        x1, y1, x2, y2 = self.p1.x, self.p1.y, self.p2.x, self.p2.y
        d = dist(x1, y1, x2, y2)
        with pushMatrix():
            translate(x2, y2)
            angle = atan2(x1 - x2, y2 - y1)
            rotate(angle)
            offset = -tamanho * .6
            head = 6
            line(0, offset, 0, -d - offset)
            line(0, offset, -head / 3, -head + offset)
            line(0, offset, head / 3, -head + offset)
