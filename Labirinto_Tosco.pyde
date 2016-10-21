"""
Labirinto Tosco!
"""

tamanho = 30 #tamanho grade
x, y = tamanho/2,5

def setup():
    global fundo
    size(600,600)
    geraLabirinto()
    fill(128,128,255)
    noStroke()
    ellipse(width/2,height/2,30,30)
    saveFrame("data/fundo.png")
    fundo = loadImage("fundo.png")

def draw():
    background(fundo)
    fill(255,0,0)
    noStroke()
    ellipse(x,y,10,10)

def keyPressed():
    global x,y
    if keyCode == UP and moveLegal(0,-6):
        y = y - 5
    if keyCode == DOWN and moveLegal(0,6):
        y = y + 5
    if keyCode == LEFT and moveLegal(-6,0):
        x = x - 5
    if keyCode == RIGHT and moveLegal(6,0):
        x = x + 5
    if x < 0:
        x = width
    if x > width:
        x = 0
    if y < 0:
        y = height
    if y > height:
        y = 0

def moveLegal(mx,my):
    if get(x+mx,y+my) == color(0):
        return False
    else:
        return True
    
def geraLabirinto():
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
            
            if int(random(2)): 
                line (tamanho/2,0,tamanho/2,tamanho)
            else: 
                if int(random(2)):
                    line (0,tamanho/2, tamanho,tamanho/2)
                else:
                    line (0,tamanho/2, tamanho,tamanho/2)
                    line (tamanho/2,0,tamanho/2,tamanho)
            popMatrix()
