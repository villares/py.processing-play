# port of aBe Hamoid's work!
# https://discourse.processing.org/t/program-to-test-hint-with-transparency/4361
# plus a few hints from https://processing.org/reference/hint_.html

# ["name", hint_status, hint_disable_constant, hint_enable_constant]
hints = (["DEPTH_TEST", False,
          DISABLE_DEPTH_TEST, ENABLE_DEPTH_TEST],
         ["DEPTH_SORT", False,
          DISABLE_DEPTH_SORT, ENABLE_DEPTH_SORT],
         ["DEPTH_MASK", False,
          DISABLE_DEPTH_MASK, ENABLE_DEPTH_MASK],
         ["OPTIMIZED_STROKE", False,
          DISABLE_OPTIMIZED_STROKE, ENABLE_OPTIMIZED_STROKE],
         ["STROKE_PERSPECTIVE", False,
          DISABLE_STROKE_PERSPECTIVE, ENABLE_STROKE_PERSPECTIVE],
         )

def setup():
    size(800, 600, P3D)
    for _, _, disable_const, _ in hints:
        hint(disable_const)

def draw():
    background(255)

    fill(0)
    for i, (name, status, _, _) in enumerate(hints):
        text("{} {}".format(name, str(status)), 20, 20 + i * 20)
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
    if id < len(hints):
        hints[id][1] = not hints[id][1]

    for _, status, disable_const, enable_const in hints:
        hint(enable_const if status else disable_const)
