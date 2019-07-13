# Code by George Profenza https://stackoverflow.com/users/89766/george-profenza
# https://stackoverflow.com/questions/56999816/is-it-possible-to-use-jcsg-library-with-processing

# You'll need to copy these libs into your Processing libraries folder: 
add_library('VVecMath')
add_library('jcsg')

def setup():
    global csgResult # the PShape reference which will contain the converted

    size(600, 500, P3D)
    noStroke()
    # Jsample code:
    # we use cube and sphere as base geometries
    cube = Cube(2).toCSG()
    sphere = Sphere(1.25).toCSG()

    # perform union, difference and intersection
    cubePlusSphere = cube.union(sphere)
    cubeMinusSphere = cube.difference(sphere)
    cubeIntersectSphere = cube.intersect(sphere)

    # translate geometries to prevent overlapping
    union = cube.union(sphere.transformed(
        Transform.unity().translateX(3))).union(
        cubePlusSphere.transformed(
        Transform.unity().translateX(6))).union(
        cubeMinusSphere.transformed(
        Transform.unity().translateX(9))).union(
        cubeIntersectSphere.transformed(
            Transform.unity().translateX(12)))

    # translate merged geometry back by half the total translation to pivot
    # around centre
    union = union.transformed(Transform.unity().translateX(-6))

    # Convert to PShape -> Note: units are small so we scale them up
    # so the shapes are visible in Processing
    csgResult = CSGToPShape(union, 45)


# re-usable function to convert a mesh to a Processing PShape
def CSGToPShape(mesh, scale):
    """Converts a CSG to a PShape"""
    # allocate a PShape group
    csgResult = createShape(GROUP)
    # for each polygon (Note: these can have 3,4 or more vertices)
    for p in mesh.getPolygons():
        # make a child PShape
        polyShape = createShape()
        # begin setting vertices to it
        polyShape.beginShape()
        # for each vertex in the polygon
        for v in p.vertices:
            # add each (scaled) polygon vertex
            polyShape.vertex(v.pos.getX() * scale,
                             v.pos.getY() * scale,
                             v.pos.getZ() * scale)

        # finish this polygon
        polyShape.endShape()
        # append the child PShape to the parent
        csgResult.addChild(polyShape)

    return csgResult


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, 0)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))
    shape(csgResult)


def keyPressed():
    saveFrame("###.png")
