from Classes import *

def setup():
    global bola1, bola2, limpa_tela
    size(300,200)
    bola1 = Bola(20, 10, 5, 255)
    bola2 = Bola(70, 50, 2, color(255,10,200))
    limpa_tela = True
         
def draw():
    if limpa_tela:
        background(0)
    bola1.mostra()
    bola2.mostra()
    bola1.anda()
    bola2.anda()

def mousePressed():
    bola1.cor = color(random(255),random(255),random(255))
    bola2.cor = color(random(255),random(255),random(255))
    
def keyPressed():
    global limpa_tela
    limpa_tela = not limpa_tela