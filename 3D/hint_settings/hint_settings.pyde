# port of aBe Hamoid's work!
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361
# plus a few hints from https://processing.org/reference/hint_.html

tests = ((DISABLE_DEPTH_TEST, ENABLE_DEPTH_TEST, "DEPTH_TEST"),
         (DISABLE_DEPTH_SORT, ENABLE_DEPTH_SORT, "DEPTH_SORT"),
         (DISABLE_DEPTH_MASK, ENABLE_DEPTH_MASK, "DEPTH_MASK"),
         (DISABLE_OPTIMIZED_STROKE, ENABLE_OPTIMIZED_STROKE,
          "OPTIMIZED_STROKE"),
         (DISABLE_STROKE_PERSPECTIVE, ENABLE_STROKE_PERSPECTIVE,
          "STROKE_PERSPECTIVE"),
         )

b = [False] * len(tests) # list of booleans to toggle hint tests

def setup():
    size(800, 600, P3D)
    for disable_hint, _, _ in tests:
        hint(disable_hint)

def draw():
    background(255)

    fill(0)
    for i, (_, _, name) in enumerate(tests):
        text("{} {}".format(name, str(b[i])), 20, 20 + i * 20)
    text("<- use the mouse to toggle settings", 200, 40)

    fill(255, 40, 20, 100)
    translate(width / 2, height / 2)
    rotateY(frameCount * 0.005)

    for x in range(-200, 201, 200):
        for y in range(-200, 201, 200):
            pushMatrix()
            translate(x, 0, y)
            box(180)
            popMatrix()

def mousePressed():
    id = mouseY / 20
    if id < len(b):
        b[id] = not b[id]

    for i, (disable_hint, enable_hint, _) in enumerate(tests):
        hint(enable_hint if b[i] else disable_hint)
 
