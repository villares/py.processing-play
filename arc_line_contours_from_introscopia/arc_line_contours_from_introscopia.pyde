# código do John - https://github.com/Introscopia

r = 100
P, a = [], [0] * 3
md = -1

def setup():
    global d
    size(500, 500)
    d = 2 * r
    P.append(PVector(250, 150))
    
    P.append(PVector(250 + 100 * cos(PI / 6.0),
                     250 + 100 * sin(PI / 6.0)))
    P.append(PVector(250 - 100 * cos(PI / 6.0),
                     250 + 100 * sin(PI / 6.0)))
    
def draw():
    background(230)
    for i in range(3):
        ellipse(P[i].x, P[i].y, 10, 10)
        
    a[0] = atan2(P[1].y - P[0].y, P[1].x - P[0].x) - HALF_PI
    a[1] = atan2(P[2].y - P[1].y, P[2].x - P[1].x) - HALF_PI
    a[2] = atan2(P[0].y - P[2].y, P[0].x - P[2].x) - HALF_PI
    
    noFill()
    start = a[2] if a[2] < a[0] else a[2] - TWO_PI
    arc(P[0].x, P[0].y, d, d, start, a[0])
    line(P[0].x + r * cos(a[0]), P[0].y + r * sin(a[0]),
         P[1].x + r * cos(a[0]), P[1].y + r * sin(a[0]))
    
    start = a[0] if a[0] < a[1] else a[0] - TWO_PI
    arc(P[1].x, P[1].y, d, d, start, a[1])
    line(P[1].x + r * cos(a[1]), P[1].y + r * sin(a[1]),
         P[2].x + r * cos(a[1]), P[2].y + r * sin(a[1]))
    
    start = a[1] if a[1] < a[2] else a[1] - TWO_PI
    arc(P[2].x, P[2].y, d, d, start, a[2])
    line(P[2].x + r * cos(a[2]), P[2].y + r * sin(a[2]),
         P[0].x + r * cos(a[2]), P[0].y + r * sin(a[2]))

def mouseWheel(E):
    global r, d
    r += 5 * E.getAmount()
    d = 2 * r

def mousePressed():
    global md
    for i in range(3):
        if dist(mouseX, mouseY, P[i].x, P[i].y) < 10:
            md = i
            break

def mouseDragged():
    if md >= 0:
        P[md].x, P[md].y = mouseX,  mouseY

def mouseReleased():
    global md
    md = -1
