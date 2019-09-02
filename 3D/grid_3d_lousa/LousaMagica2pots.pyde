# Licença GPL3 - mas atribuição é apreciada!
"""
Desenho com potenciômetros 
    Arduino + Firmata All Inputs + Potenciômetros
    Alexandre Villares http://abav.lugaralgum.com
    arteprog - arte e programação http://arteprog.space
    Apresentada originalmente na inauguraço do SESC 24 de maio com Estúdio Hacker
    http://estudiohacker.io
    http://twitter.com/estudiohacker
"""

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta_serial in enumerate(Arduino.list()):  # Enumera portas seriais
    println(str(num)+":"+porta_serial)               # Mostra no console
NUM_PORTA = 0  # Precisa mudar! Leia a lista no console para descobrir
    
def setup():
    global arduino
    size(1024, 1024)
    colorMode(HSB)  # para usar HSB em vez de RGB!
    frameRate(30)
    noStroke()
    background(0)
    arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)

def draw():
    X = arduino.analogRead(5)  # pino A5 (analógico)
    Y = arduino.analogRead(0)
    tam = 20  # Tamanho
    sat = 255  # Saturação
    opa = 255  # Opacidade/Alpha
    F = frameCount
    # Note modo HSB no setup! (Matiz, Saturação, Brilho, Alfa)
    fill(F % 255, sat, 255, opa)
    ellipse(X, Y, tam, tam)
    if keyPressed:
        background(0)  # limpa o canvas com preto
