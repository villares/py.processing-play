""" Pong Procedural
    Esta estrutura deve facilitar uma futura refacção orientada a objetos
    Teclas 'a' e 'z' controlam um jogador, as setas para cima e para baixo o outro.
*** Tecla 'espaço' para iniciar o ponto.
"""

DIA_BOLA = 10
VEL_INICIAL = 4
MEIO_JOGADOR = 50
ESP_JOGADOR = 10
VEL_JOGADOR = 5

def setup():
    global velX, velY
    size(600, 400)
    noStroke()
    prepara_jogo()    # prepara o jogo, esta função normalmente recomeça o jogo
    velX, velY = 0, 0  # mas aqui eu logo em seguida paro a bola zerando as velocidades                                                                                                                                                                                           

def draw():
    background(0)
    if not game_over:
            jogadores_move()
            jogadores_desenha()
            bola_move()
            bola_desenha()
    else:
            escreve_game_over()
   
     
def keyPressed():
    global sobe_1, desce_1, sobe_2, desce_2
    if key == 'a':
            sobe_1 = True
    elif key == 'z':
            desce_1 = True
    if keyCode == UP:
            sobe_2 = True
    elif keyCode == DOWN:
            desce_2 = True
    if key == ' ':
            prepara_jogo()

   
def keyReleased():
    global sobe_1, desce_1, sobe_2, desce_2
    if key == 'a':
            sobe_1 = False
    elif key == 'z':
            desce_1 = False
    if keyCode == UP:
            sobe_2 = False
    elif keyCode == DOWN:
            desce_2 = False   
        
def bola_move():
    global bolaX, bolaY, velX, velY, game_over
    bolaX, bolaY = bolaX + velX, bolaY + velY    # altera posição x e y da bola usando as velocidades x e y
    if not(0 < bolaX < width):                      # se a bola sair da tela à direita ou à esquerda
            if jogador_rebate(1) or jogador_rebate(2):  # se for rebatida pelo jogador 1 ou 2
              velX = -velX               # inverta a velocidade horizontal
            else:                          # senão: 
              game_over = True          # game over!
    if not(0 < bolaY < height):   # se sair da tela por cima ou por baixo
            velY = -velY            # inverta a velocidade vertical
                    
def bola_desenha():
    fill ( 255,0,0)
    ellipse(bolaX, bolaY, DIA_BOLA, DIA_BOLA)           

def jogadores_move():
    global j1Y, j2Y
    if sobe_1: j1Y = j1Y - VEL_JOGADOR
    if desce_1: j1Y = j1Y + VEL_JOGADOR
    if sobe_2: j2Y = j2Y - VEL_JOGADOR
    if desce_2: j2Y = j2Y + VEL_JOGADOR
                
def jogadores_desenha():
    fill(0,0,255)
    rect (0, j1Y - MEIO_JOGADOR,
           ESP_JOGADOR, MEIO_JOGADOR*2)
    rect (width - ESP_JOGADOR, j2Y - MEIO_JOGADOR,
           ESP_JOGADOR, MEIO_JOGADOR*2)   

def prepara_jogo():     # começa ou recomeça um jogo
    global game_over
    global bolaX, bolaY, velX, velY
    global sobe_1, desce_1, sobe_2, desce_2
    global j1Y, j2Y #, j1_points, j2_points
    bolaX, bolaY = width/2, height/2
    velX = (-VEL_INICIAL, VEL_INICIAL)[int(random(2))]
    velY = (-VEL_INICIAL, VEL_INICIAL)[int(random(2))]
    sobe_1 = desce_1 = sobe_2 = desce_2 = False
    j1Y = j2Y = height/2                                                           
    #j1_pontos = j2_pontos = 0
    game_over = False
           
def escreve_game_over():
    textSize(60)
    textAlign(CENTER)
    text("GAME OVER", width/2, height/2)
    
def jogador_rebate(jogador): # checa se jogador 1 ou 2 rebateu com sucesso a bola
    if jogador == 1:
            return (bolaX <= 0 and
                    j1Y - MEIO_JOGADOR < bolaY < j1Y + MEIO_JOGADOR)    
    else:
            return (bolaX >= width and
                    j2Y - MEIO_JOGADOR < bolaY < j2Y + MEIO_JOGADOR) 
