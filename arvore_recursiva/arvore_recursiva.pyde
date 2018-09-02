def setup():
    size(500, 500)

def draw():
    background(200)
    branch(250, 300, 50)
    noLoop()

def branch(x, y, siz):
    shrink = 5
    ang = 30
    ang_rnd = 15
    if siz > 1:
        with pushMatrix():
            translate(x, y)
            rotate(radians(-ang + random(-ang_rnd, ang_rnd)))
            strokeWeight(siz * .1)
            line(0, 0, 0, -siz)
            branch(0, -siz, siz - shrink)
        with pushMatrix():
            translate(x, y)
            rotate(radians(+ang + random(-ang_rnd, ang_rnd)))
            strokeWeight(siz * .1)
            line(0, 0, 0, -siz)
            branch(0, -siz, siz - shrink)
            
def keyPressed():
    loop()
