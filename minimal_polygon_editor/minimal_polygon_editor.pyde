"""
A minimal poly editor
"""
ORDER = 10
click = False
cell_size = 45.
pts = [(0.0, 4.0), (4.0, 4.0), (0.0, 8.0), (4.0, 8.0), (2.0, 12.0),
       (8.0, 6.0), (4.0, 6.0), (8.0, 2.0), (4.0, 2.0), (6.0, -2.0)]

def setup():
    global xo, yo  # offset de correção da borda na tela cheia
    global cell_size, grid_size
    size(500, 500, P2D)
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
            cell(x, y)
    poly_draw()

def cell(mx, my):
    global click
    stroke(128)
    if dist(mouseX - xo, mouseY - yo, mx, my) < cell_size / 2:
        fill(209)
        if click:
            x = mx / cell_size * 2 - ORDER / 2
            y = my / cell_size * 2 - ORDER / 2
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
            sx = (x + ORDER / 2) * cell_size / 2
            sy = (y + ORDER / 2) * cell_size / 2
            vertex(sx, sy)
        endShape(CLOSE)
    elif len(pts) == 2:
        beginShape(LINES)
        for x, y in pts:
            sx = (x + ORDER / 2) * cell_size / 2
            sy = (y + ORDER / 2) * cell_size / 2
            vertex(sx, sy)
        endShape()
    popStyle()

def mouseReleased():
    global click
    if mouseButton == LEFT:
        click = True

def keyPressed():
    global pts
    if key == " ":
        pts = []  # empty pts
    if key == "p":
        println(pts)    
