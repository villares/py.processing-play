""" Alexandre B A Villares - http://abav.lugaralgum.com
    Brincando com uma lista de pontos, e agora arestas.
    Para rodar, instale o Processing Modo Python.
    Desenvolvido principalmente durante o Carnahacking 2017
    no Garoa Hacker Clube - http://garoa.net.br
    e publicado em https://github.com/villares/py.processing-play
"""
import random as rnd

pontos = set()  # conjunto de Pontos
arestas = []    # lista de Arestas

# tamanho dos Pontos (influi no 'mouse over' e offset das setas)
tamanho = 50
barra = 100
velocidade = 1  # para sorteio de velocidades iniciais random(+v,-v)
velocidade_maxima = 1 
pontos_iniciais = 5

def setup():
    size(600, 600)
    strokeWeight(2)
    for _ in range(pontos_iniciais):
        x, y = random(width), random(height)
        cor = cor_rnd()  # sorteia uma cor
        pontos.add(Ponto(x, y, cor))  # acrescenta um Ponto

def draw():
    background(128)        # limpa a tela
    for aresta in arestas:  # checa se há Arestas com Pontos já removidos
        if (aresta.p1 not in pontos) or (aresta.p2 not in pontos):
            arestas.remove(aresta)   # nesse caso remove a Aresta também
            # print(aresta.p1, aresta.p2)
        else:                # senão
            aresta.desenha()  # desenha a Aresta com uma seta!
            aresta.puxa_empurra()
    for ponto in pontos:  # cada Ponto desenha e atualiza sua posição
        ponto.desenha()
        ponto.move()
        ponto.vx = limitar(ponto.vx, velocidade_maxima)
        ponto.vy = limitar(ponto.vy, velocidade_maxima)

def cor_rnd(alpha_value=128):       # helper para sortear uma cor
    return color(random(128, 255), random(128, 255), random(128, 255), alpha_value)

# Sob clique do mouse seleciona/deseleciona Pontos ou Arestas
def mouseClicked():
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < tamanho * 3 / 2:
            ponto.sel = not ponto.sel  # inverte status de seleção
    mouse = PVector(mouseX, mouseY)
    for aresta in arestas:    # para cada Aresta checa o 'mouse over'
        if pointInsideLine(mouse, aresta.p1, aresta.p2, 6):
            aresta.sel = not aresta.sel  # inverte status de seleção


def keyPressed():   # Quando uma tecla é pressionada
    # barra de espaço acrescenta Pontos na posição atual do mouse
    if key == ' ':
        pontos.add(Ponto(mouseX, mouseY, cor_rnd()))  # acrescenta Ponto no set
    # 'd' remove os Pontos previamente selecionandos com clique, marcados em preto.
    if key == 'd':
        for ponto in pontos:
            # se a lista tiver pelo menos 2 pontos
            if ponto.sel and len(pontos) > 1:
                pontos.remove(ponto)           # remove pontos selecionados
        for aresta in arestas:
            if aresta.sel:  # se a lista tiver pelo menos 2 pontos
                arestas.remove(aresta)           # remove pontos selecionados

def mouseDragged():        # quando o mouse é arrastado
    for ponto in pontos:   # para cada Ponto checa distância do mouse
        if dist(mouseX, mouseY, ponto.x, ponto.y) < tamanho * 3 / 2:
            # move o Ponto para posição do mouse
            ponto.x, ponto.y = mouseX, mouseY
            ponto.vx = 0
            ponto.vy = 0

class Ponto():

    " Pontos num grafo, velocidade inicial sorteada, criam Arestas com outros Pontos "

    def __init__(self, x, y, cor=color(0)):
        self.x = x
        self.y = y
        self.z = 0  # para compatibilidade com PVector...
        self.cor = cor
        self.vx = random(-velocidade, velocidade)
        self.vy = random(-velocidade, velocidade)
        self.sel = False   # se está selecionado
        self.cria_arestas()

    def desenha(self):
        fill(self.cor)
        if self.sel:
            stroke(0)
        else:
            noStroke()
        ellipse(self.x, self.y, tamanho, tamanho)
        if dist(mouseX, mouseY, self.x, self.y) < tamanho:
            stroke(255)
            # text(str(len(pontos)) + " " + str(len(arestas)), self.x, self.y)
            ellipse(self.x, self.y, tamanho+5, tamanho+5)


    def move(self):
        self.x += self.vx
        self.y += self.vy
        if not (0 < self.x < width):
            self.vx = -self.vx
        if not (0 < self.y < height):
            self.vy = -self.vy
        # self.p1.vx = limitar(self.p1.vx, 3)
        # self.p1.vy = limitar(self.p1.vy, 3)
        # self.p2.vx = limitar(self.p2.vx, 3)
        # self.p2.vy = limitar(self.p2.vy, 3)

    def cria_arestas(self, modo='random'):
        if modo == 'random':
            lista_pontos = list(pontos)
            if lista_pontos:
                nova_aresta = Aresta(rnd.choice(lista_pontos), self)
                arestas.append(nova_aresta)
        elif modo == 'all':
             for ponto in pontos:
                nova_aresta = Aresta(ponto, self)
                arestas.append(nova_aresta)

class Aresta():

    """ Arestas contém só dois Pontos e podem ou não estar selecionadas """

    def __init__(self, p1, p2):
        self.p1 = p1
        self.p2 = p2
        self.sel = False

    def desenha(self):
        if self.sel:
            stroke(0)
        else:
            stroke(255)
        line(self.p1.x, self.p1.y, self.p2.x, self.p2.y)

    def puxa_empurra(self):
        d = dist(self.p1.x, self.p1.y, self.p2.x, self.p2.y)
        delta = barra - d
        dir = PVector.sub(self.p1, self.p2)
        dir.mult(delta / 1000)
        self.p1.vx = self.p1.vx + dir.x
        self.p1.vy = self.p1.vy + dir.y
        self.p2.vx = self.p2.vx - dir.x
        self.p2.vy = self.p2.vy - dir.y


def limitar(v, v_max):
    if v > v_max:
        return v_max
    elif v < -v_max:
        return -v_max
    else:
        return v

def pointInsideLine(thePoint, theLineEndPoint1, theLineEndPoint2, theTolerance):
    # from Andreas Schlegel / http://www.sojamo.de """
    dir = PVector(theLineEndPoint2.x, theLineEndPoint2.y, 0)
    dir.sub(theLineEndPoint1)
    diff = PVector(thePoint.x, thePoint.y, 0)
    diff.sub(theLineEndPoint1)
    try:
        insideDistance = diff.dot(dir) / dir.dot(dir)
    except ZeroDivisionError:
        insideDistance = 1000
    if (0 < insideDistance < 1):
        closest = PVector(theLineEndPoint1.x, theLineEndPoint1.y, 0)
        dir.mult(insideDistance)
        closest.add(dir)
        d = PVector(thePoint.x, thePoint.y)
        d.sub(closest)
        distsqr = d.dot(d)
        return (distsqr < pow(theTolerance, 2))
    return False
