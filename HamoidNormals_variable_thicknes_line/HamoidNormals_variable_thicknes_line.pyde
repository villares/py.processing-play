"""
Giving variable thickness to a line (calculating normals), based on code by Hamoid at:
https://discourse.processing.org/t/giving-variable-thickness-to-a-line-calculating-normals/5890
"""

points = []

def setup():
    size(400, 400)
    # 1. Define polyline points
    points.append(PVector(61, 183))
    points.append(PVector(108, 113))
    points.append(PVector(193, 118))
    points.append(PVector(256, 158))
    points.append(PVector(248, 239))
    points.append(PVector(258, 310))
    points.append(PVector(328, 353))
    points.append(PVector(377, 341))
    calculate()

def keyPressed():
    calculate()

def calculate():
    global normals
    # 2. calculations

    # Ensure normals has the same size as points
    normals = [PVector()] * len(points)

    # Calculate normals
    for i in range(len(points) - 1):
        # sub = PVector.sub(points[i], points[i + 1])
        sub = points[i] - points[i + 1]
        normals[i] = PVector(-sub.y, sub.x)

    for i in range(1, len(points)):
        # sub = PVector.sub(points[i], points[i - 1])
        # normals[i].add(PVector(sub.y, -sub.x))
        sub = points[i] - points[i - 1]
        normals[i] += PVector(sub.y, -sub.x)

    # Resize normals
    for n in normals:
        n.normalize().mult(random(10, 30))


def draw():
    background(255)
    # draw calculated thick line
    if mousePressed:
        stroke(0)
    else:
        noStroke()
    fill("#FFCC00")
    with beginShape(QUAD_STRIP):
        for (p, n) in zip(points, normals):
            vertex(p.x + n.x, p.y + n.y)
            vertex(p.x - n.x, p.y - n.y)

    # draw the original line
    stroke("552200")
    noFill()
    with beginShape():
        for p in points:
            vertex(p.x, p.y)

    # draw line vertices
    stroke("#552200")
    strokeWeight(2)
    fill(255)
    for p in points:
        ellipse(p.x, p.y, 6, 6)

    # draw contour points
    # noStroke()
    stroke(0)
    fill("#883300")
    for (p, n) in zip(points, normals):
        ellipse(p.x + n.x, p.y + n.y, 3, 3)
        ellipse(p.x - n.x, p.y - n.y, 3, 3)
