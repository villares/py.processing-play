def setup():
    size(500, 500)

def draw():
    background(200)
    branch(250, 300, 50)
    noLoop()

def branch(x, y, siz):  # falho
    shrink = 5 # encolhimento
    ang = 30 # ângulo
    ang_rnd = 15 # faixa de randomização do ângulo
    pushMatrix()
    translate(x, y)
    if siz > 1:
        rotate(radians(-ang * 1 + random(-ang_rnd, ang_rnd)))
        strokeWeight(siz * .1)
        line(0, 0, 0, -siz)
        branch(0, -siz, siz - shrink)
        rotate(radians(+ang * 2 + random(-ang_rnd, ang_rnd)))
        strokeWeight(siz * .1)
        line(0, 0, 0, -siz)
        branch(0, -siz, siz - shrink)
    popMatrix()

def keyPressed():
    loop()
