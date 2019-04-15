
"""
a minimal poly editor
"""

ORDER = 10
pts = [(2.5, 3.5), (5.5, 3.5), (2.5, 5.5),
       (5.5, 5.5), (2.5, 7.5), (5.5, 7.5),
       (3.5, 9.5), (8.5, 6.5), (5.5, 6.5),
       (8.5, 4.5), (5.5, 4.5), (8.5, 2.5),
       (5.5, 2.5), (7.5, 0.5)]
click = False
cell_size = 50.

def setup():
    global xo, yo  # offset de correção da borda na tela cheia
    global cell_size, grid_size
    size(600, 600, P2D)
    grid_size = ORDER * cell_size
    xo, yo = (width - grid_size) / 2, (height - grid_size) / 2
    rectMode(CENTER)

def draw():
    background(255)
    translate(xo, yo)

    # grade de cellulas
    for i in range(ORDER):
        x = cell_size / 2 + i * cell_size
        for j in range(ORDER):
            y = cell_size / 2 + j * cell_size
            pos = i + j * 5
            cell(x, y)
    poly_draw()

def cell(mx, my):
    global click
    stroke(128)
    if dist(mouseX - xo, mouseY - yo, mx, my) < cell_size / 2:
        fill(209)
        if click:
            x, y = mx / cell_size, my / cell_size
            if (x, y) in pts:
                pts.remove((x, y))
            else:
                pts.append((x, y))
            click = False
    else:
        fill(255)
    rect(mx, my, cell_size, cell_size)

def poly_draw():
    #  polígono
    pushStyle()
    strokeWeight(3)  # espessura do polígono
    noFill()
    if len(pts) >= 3:
        beginShape()
        for x, y in pts:
            stroke(0)
            sx = (x) * cell_size
            sy = (y) * cell_size
            vertex(sx, sy)
        endShape(CLOSE)
    elif len(pts) == 2:
        beginShape(LINES)
        for x, y in pts:
            sx = (x) * cell_size
            sy = (y) * cell_size
            vertex(sx, sy)
        endShape(CLOSE)
    popStyle()


def mouseReleased():
    global click
    if mouseButton == LEFT:
        click = True

def keyPressed():
    if key == " ":
        reset()
    if key == "p":
        println(pts)

def reset():
    global pts
    pts = []  # esvazia lista de pts
