""" Alexandre B A Villares - abav.lugaralgum.com
    Brincando com uma lista de pontos --> github.com/villares
"""
lista = [] # lista de pontos
TAM = 10   # tamanho 

def setup():
    #fullScreen()
    size(600, 800)
    stroke(255)
    fill(0)
    for _ in range(10):
        x, y = random(width), random(height)
        lista.append((x,y)) # acrescenta uma tupla na lista
    
def draw():
    background(0)
    for x1, y1 in lista:
        for x2, y2 in lista:
            line (x1, y1, x2, y2)
            ellipse(x2, y2, TAM, TAM)
        
def mousePressed():
    lista.append((mouseX,mouseY))

def keyPressed():
    if len(lista) > 1:
        ultimo = lista.pop(0)
        print(ultimo)

    
        
        
