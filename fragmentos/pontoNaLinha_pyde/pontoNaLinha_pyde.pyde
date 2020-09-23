TOLERANCE = EPSILON

def setup():
    global p1, p2, mouse
    size(500, 500)
    background(0)
    noSmooth()

def draw():
    s = 2  # scale factor
    scale(s)
    mouse = PVector(mouseX, mouseY) / s

    stroke(255)
    p1 = PVector(50, 50)
    p2 = PVector(150, 150)
    if pointInsideLine(mouse, p1, p2,
                       TOLERANCE) == True:
        stroke(255, 0, 0)
        point(mouse.x, mouse.y)
        stroke(0, 255, 0)
    line(p1.x, p1.y, p2.x, p2.y)

    stroke(255)
    p1x, p1y = 50, 100
    p2x, p2y = 150, 200
    if point_over_line(mouse.x, mouse.y,
                       p1x, p1y, p2x, p2y,
                       TOLERANCE) == True:
        stroke(255, 0, 0)
        point(mouse.x, mouse.y)
        stroke(0, 0, 255)
    line(p1x, p1y, p2x, p2y)


def point_over_line(px, py, lax, lay, lbx, lby,
                    tolerance=EPSILON):
    """
    Check if point is over line using the sum of
    the distances from the point to the line ends
    (the result has to be near equal for True).
    """
    ab = dist(lax, lay, lbx, lby)
    pa = dist(lax, lay, px, py)
    pb = dist(px, py, lbx, lby)
    return (pa + pb) <= ab + tolerance / 100.0

def points_are_colinear(ax, ay, bx, by, cx, cy,
                        tolerance=EPSILON):
    """
    Test for colinearity by calculating the area
    of a triangle formed by the 3 points.
    """
    area = triangle_area((ax, ay), (bx, by), (cx, cy))
    return abs(area) < tolerance


def triangle_area(p0, p1, p2):
    a = (p1[0] * (p2[1] - p0[1]) +
         p2[0] * (p0[1] - p1[1]) +
         p0[0] * (p1[1] - p2[1]))
    return a

def pointInsideLine(thePoint, theLineEndPoint1, theLineEndPoint2, theTolerance=2):
    """
    Code from Andreas Schlegel / http://www.sojamo.de
    posted on https://processing.org/discourse/beta/num_1247920826.html
    ported to Python Mode by Alexandre Villares / http://abav.lugaralgum.com
    """
    dir = PVector(theLineEndPoint2.x, theLineEndPoint2.y)
    dir.sub(theLineEndPoint1)
    diff = PVector(thePoint.x, thePoint.y)
    diff.sub(theLineEndPoint1)
    # inside distance determines the weighting
    # between linePoint1 and linePoint2
    insideDistance = diff.dot(dir) / dir.dot(dir)
    if(insideDistance > 0 and insideDistance < 1):
        # the point is inside/close to
        # the line if insideDistance>0 or <1
        closest = PVector(theLineEndPoint1.x, theLineEndPoint1.y)
        dir.mult(insideDistance)
        closest.add(dir)
        d = PVector(thePoint.x, thePoint.y)
        d.sub(closest)
        distsqr = d.dot(d)
        # check the distance of thePoto the line against our tolerance.
        return (distsqr < pow(theTolerance, 2))
    return False
