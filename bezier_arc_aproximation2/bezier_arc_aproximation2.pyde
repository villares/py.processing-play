# Adapted from code by MenteCode: making a section of a circle with a bezier curve
# http://forum.processing.org/two/discussion/1797/how-to-use-bezier-curve-to-approximate-one-quarter-of-a-circle#Item_3

radius = 100

def setup():
    size(500, 500)

def draw():
    background(150)
    translate(width / 2, height / 2)
    noFill()
    angle = map(mouseX, 0, width, 0, 180)
    bezier_arc(angle, radius)

    # curve fit check reference
    ellipseMode(CENTER)
    stroke(255, 0, 0)
    strokeWeight(3)
    ellipse(0, 0, radius * 2, radius * 2)


def bezier_arc(angle, radius):
    lnth = 4 * tan(radians(angle / 4)) / 3
    pStart = PVector(0, -radius)
    pCtrl1 = PVector(radius * lnth, -radius)
    pCtrl2 = PVector(-radius * lnth, -radius)
    pEnd = PVector(0, -radius)

    pCtrl2.rotate(radians(angle))
    pEnd.rotate(radians(angle))

    stroke(0)
    strokeWeight(10)
    beginShape()
    vertex(pStart.x, pStart.y)
    bezierVertex(pCtrl1.x, pCtrl1.y,
                 pCtrl2.x, pCtrl2.y,
                 pEnd.x, pEnd.y)
    endShape()
    # bezier(pStart.x, pStart.y,
    #        pCtrl1.x, pCtrl1.y,
    #        pCtrl2.x, pCtrl2.y,
    #        pEnd.x, pEnd.y)

    stroke(0, 255, 0)
    strokeWeight(15)
    point(pStart.x, pStart.y)
    text("start pt", pStart.x + 8, pStart.y)
    point(pCtrl1.x, pCtrl1.y)
    text("ctrl pt1", pCtrl1.x + 8, pCtrl1.y)
    point(pCtrl2.x, pCtrl2.y)
    text("ctrl pt2", pCtrl2.x + 8, pCtrl2.y)
    point(pEnd.x, pEnd.y)
    text("end pt", pEnd.x + 8, pEnd.y)
