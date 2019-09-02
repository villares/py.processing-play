"""
Uma grade de letras
"""
from __future__ import unicode_literals

letras = "ABCDEFGHIJKLMNOPQRSTUVWXYZ☂#$*&"

def setup():
    size(640, 360)
    background(0)
    # Criar uma fonte PFont
    printArray(PFont.list())  # lista de fontes do computador
    f = createFont("GaroaHackerClubeBold.otf", 24)
    textFont(f)
    textAlign(CENTER, CENTER)
    textSize(24)
    frameRate(2)

def draw():
    background(0)
    passo = 22
    for y in range(12, height, passo):
        for x in range(12, width, passo):
            sorteio = int(random(len(letras)))
            letter = letras[sorteio]
            if (letter == '☂' or letter == '&'):
                fill(0, 200, 0)
            else:
                fill(255)
            # Desenha a letra na tela
            text(letter, x, y)
