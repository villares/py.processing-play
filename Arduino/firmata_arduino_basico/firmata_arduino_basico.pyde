""" 
Código para a leitura dos potenciômetros, requer biblioteca Firmata (Arduino)
Você deve ajustar o valor de SERIAL para porta USB com seu Arduino
No Linux pode ser que precise fazer sudo chmod 666 /dev/ttyUSB0 (ou equivalente).
"""
# ARDUINO
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta in enumerate(Arduino.list()):  # Enumera portas seriais
    println(str(num)+":"+porta)               # Mostra no console
NUM_PORTA = 0  # Precisa mudar! Leia a lista no console para descobrir

def setup():
    size(600, 400)  # tamanho da tela
    global arduino
    arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)

def draw():
    background(0)  # limpa a tela
    # CÍRCULO AMARELO
    POT_0 = arduino.analogRead(0) / 2
    fill(255, 255, 0, 200)  # fill(vermelho->255, verde->255, azul->0) -> Amarelo
    ellipse(200,         # x
            200,         # y
            POT_0,  # largura 
            POT_0)  # altura
    # CÍRCULO VERDE
    POT_5 = arduino.analogRead(5) / 2
    fill(0, 255, 0, 200)  # fill(vermelho->0, verde->255, azul->0) -> Verde
    ellipse(width - 200,  # x
            200,          # y
            POT_5,     # largura
            POT_5)     # altura