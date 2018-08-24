def setup():
    size(500, 500)
    frameRate(5)

def draw():
    background(200)
    galho(250, 300, 50)
    noLoop()

def galho(x, y, tam):
    encurtamento = 5
    if tam > 1:
        with pushMatrix():
            translate(x, y)
            with pushMatrix():
                rotate(radians(-30 + random(-15, 15)))
                strokeWeight(tam * .1)
                line(0, 0, 0, -tam)
                galho(0, -tam, tam - encurtamento)
            with pushMatrix():
                rotate(radians(+30 + random(-15, 15)))
                strokeWeight(tam * .1)
                line(0, 0, 0, -tam)
                galho(0, -tam, tam - encurtamento)
                
def keyPressed():
    loop()
