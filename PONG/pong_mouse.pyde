""" 
Jogo PONG! com apenas um ponto. 
O mouse controla o jogador amarelo.
Vamos usar como base para nossas alterações!
"""

# JOGADORES
MEIA_ALTURA_JOGADOR = 50
LARGURA_JOGADOR = 10

# BOLA
BOLA_TAMANHO = 20

def setup():
    size(600, 400)  # tamanho da tela
    # BOLA
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2  # Bola no meio da tela
    BOLA_VEL_X, BOLA_VEL_Y = 0, 0  # Bola parada

def draw():
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    background(0)  # limpa a tela

    # JOGADORES
    AMARELO_Y = mouseY  # jogador amarelo segue o mouse!
    fill(255, 255, 0)  # Amarelo fill(vermelho->255, verde->255, azul->0)
    rect(0,           # rect(x, y, largura, altura)
         AMARELO_Y - MEIA_ALTURA_JOGADOR,
         LARGURA_JOGADOR,
         MEIA_ALTURA_JOGADOR * 2)
    VERDE_Y = BOLA_Y  # jogador verde segue a bola!
    fill(0, 255, 0)   # Verde fill(vermelho->0, verde->255, azul->0)
    rect(width - LARGURA_JOGADOR,
         VERDE_Y - MEIA_ALTURA_JOGADOR,
         LARGURA_JOGADOR,
         MEIA_ALTURA_JOGADOR * 2)

    # BOLA
    BOLA_X = BOLA_X + BOLA_VEL_X  # atualiza posição horizontal (x) da bola
    BOLA_Y = BOLA_Y + BOLA_VEL_Y  # atualiza posição vertical (y) da bola
    fill(255)  # cor de preenchimento branco, equivale fill(255, 255, 255)
    ellipse(BOLA_X, BOLA_Y, BOLA_TAMANHO, BOLA_TAMANHO)  # desenha a bola
    if BOLA_X < 0:  # Se a bola sair da tela pela esquerda
        if AMARELO_Y - MEIA_ALTURA_JOGADOR < BOLA_Y < AMARELO_Y + MEIA_ALTURA_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X  # rebate
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0  # para a bola
    if BOLA_X > width:  # Se a bola sair da tela pela direita
        if VERDE_Y - MEIA_ALTURA_JOGADOR < BOLA_Y < VERDE_Y + MEIA_ALTURA_JOGADOR:
            BOLA_VEL_X = -BOLA_VEL_X  # rebate
        else:
            BOLA_VEL_X, BOLA_VEL_Y = 0, 0  # para a bola
    if BOLA_Y < 0:  # Se a bola sair da tela por cima
        BOLA_VEL_Y = -BOLA_VEL_Y
    if BOLA_Y > height:  # Se a bola sair da tela por baixo
        BOLA_VEL_Y = -BOLA_VEL_Y

def keyPressed():  # 'reset' quando apertar uma tecla
    global BOLA_X, BOLA_Y, BOLA_VEL_X, BOLA_VEL_Y
    BOLA_X, BOLA_Y = width / 2, height / 2  # Bola no meio da tela
    # Sorteio da velocidade horizontal da bola
    BOLA_VEL_X = (-4, 4)[int(random(2))]
    # Sorteio da velocidade vertical da bola
    BOLA_VEL_Y = (-4, 4)[int(random(2))]