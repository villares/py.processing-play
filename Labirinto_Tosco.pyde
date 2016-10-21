"""
Labirinto Tosco!
"""

tamanho = 30 # tamanho das células da grade
x, y = tamanho/2,5 # posiciona toscamente o x e y do jogador

def setup():
    global fundo
    size(600,600)
    geraLabirinto() 
    fill(128,128,255)
    noStroke()
    ellipse(width/2,height/2,30,30) # meio, alvo, meta, objetivo - vitória não implementada ainda
    saveFrame("data/fundo.png")
    fundo = loadImage("fundo.png") # acho que tem um jeito melhor de fazer isso, mas eu não lembro

def draw():
    background(fundo) # limpa redraw usando fundo
    fill(255,0,0)
    noStroke()
    ellipse(x,y,10,10) # desenha jogador

def keyPressed(): # move jogador
    global x,y
    if keyCode == UP and moveLegal(0,-6):
        y = y - 5
    if keyCode == DOWN and moveLegal(0,6):
        y = y + 5
    if keyCode == LEFT and moveLegal(-6,0):
        x = x - 5
    if keyCode == RIGHT and moveLegal(6,0):
        x = x + 5
    # Segue o wrap around
    if x < 0:       
        x = width
    if x > width:
        x = 0
    if y < 0:
        y = height
    if y > height:
        y = 0

def moveLegal(mx,my):
    ''' checa se a posição não invade uma parede preta''' 
    if get(x+mx,y+my) == color(0):
        return False
    else:
        return True
    
def geraLabirinto():
    ''' prepara/desenha um labirinto tosco '''
    strokeWeight(10)
    background(255)
    colunas = width / tamanho
    filas = height / tamanho
    for fila in range (filas):
        for coluna in range(colunas):   
            pushMatrix()
            translate(coluna * tamanho, fila * tamanho)
            noStroke()
            fill(random(255),50)
            rect(0,0,tamanho,tamanho)            
            stroke(0)
            if int(random(2)):  # esta é a tosca mágica hardcodada desse 'estilo' de labirinto tosco
                line (tamanho/2,0,tamanho/2,tamanho)
            else: 
                if int(random(2)):
                    line (0,tamanho/2, tamanho,tamanho/2)
                else:
                    line (0,tamanho/2, tamanho,tamanho/2)
                    line (tamanho/2,0,tamanho/2,tamanho)
            popMatrix()
