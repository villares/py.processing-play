# JCSG library adapted for use with Processing by George Profenza https://stackoverflow.com/users/89766/george-profenza
# https://stackoverflow.com/questions/56999816/is-it-possible-to-use-jcsg-library-with-processing

# You'll need to copy these libs into your Processing libraries folder: 
add_library('VVecMath')
add_library('jcsg')

def setup():
    global pshape_result
    size(600, 500, P3D)
    noStroke()
    csg_result = calculate_stuff()
    pshape_result = CSGToPShape(csg_result, 45)


def draw():
    background(0)
    lights()
    translate(width * 0.5, height * 0.5, 0)
    rotateY(map(mouseX, 0, width, -PI, PI))
    rotateX(map(mouseY, 0, height, PI, -PI))
    shape(pshape_result)


def calculate_stuff():
    # Jsample code:
    # we use cube and sphere_ as base geometries
    cube = Cube(2).toCSG()
    sphere_ = Sphere(1.25).toCSG()

    # perform union, difference and intersection
    cubePlusSphere = cube.union(sphere_) 
    cubeMinusSphere = cube.difference(sphere_)
    cubeIntersectSphere = cube.intersect(sphere_)
 
    sphere_ = csgTranslate(sphere_, 3, 0, 0)
    cubePlusSphere = csgTranslate(cubePlusSphere, 6, 0, 0)
    cubeMinusSphere = csgTranslate(cubeMinusSphere, 9, 0, 0)
    cubeIntersectSphere = csgTranslate(cubeIntersectSphere, 12, 0, 0)

    union = cube.union((sphere_,
                        cubePlusSphere,
                        cubeMinusSphere,
                        cubeIntersectSphere))

    # translate merged geometry back by half to pivot around centre
    return csgTranslate(union, -6, 0, 0)

def csgTranslate(csg, x, y, z):
    return csg.transformed(Transform.unity().translate(x, y, z))

def CSGToPShape(mesh, scale):
    """
    Convert a CSG mesh to a Processing PShape
    """
    result = createShape(GROUP)  # allocate a PShape group
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
        result.addChild(polyShape)

    return result

def keyPressed():
    saveFrame("###.png")
