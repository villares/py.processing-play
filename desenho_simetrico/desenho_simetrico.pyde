'''
Prova de conceito, programa de desenho com simetria radial
Alexandre B A Villares - http://abav.lugaralgum.com
Para rodar, instale o Processing Python Mode:
http://abav.lugaralgum.com/como-instalar-o-processing-modo-python/
DOE: http://patreon.com/arteprog
'''
divisoes = 12

def setup():
    size(500, 500)
    background(255)
    strokeWeight(5)

def draw():
    translate(width / 2, height / 2)  # este é desfeito ao final do draw
    for _ in range(divisoes):
        rotate(TWO_PI / divisoes)
        if mousePressed:
            with pushMatrix():
                translate(-width / 2, -height / 2)
                line(pmouseX, pmouseY, mouseX, mouseY)
def keyPressed():
    global divisoes
    if key in ['+', '=']: divisoes += 1
    if key == '-' and divisoes > 1: divisoes -= 1    
    if key == ' ': background(255)
    if key == '0': stroke(0)
    if key == 'r': stroke(255, 0, 0)
    if key == 'g': stroke(0, 255, 0)
    if key == 'b': stroke(0, 0, 255)
