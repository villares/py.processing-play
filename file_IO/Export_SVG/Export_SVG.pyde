"""
Minimal SVG Export test for Processing Python Mode
"""

add_library('svg')
 
def setup():
    global bg
    size(400, 400)
    background(255)
    # PGraphics pgDrawing
    pgDrawing = createGraphics(400, 400, SVG, "test.svg")
    pgDrawing.beginDraw()
    pgDrawing.background(255)
    pgDrawing.stroke(0)
    pgDrawing.strokeWeight(4)
    pgDrawing.rect(10, 10, 70, 50, 10)
    pgDrawing.endDraw()
    pgDrawing.dispose()
    # Load PShape bg
    bg = loadShape("test.svg")

 
def draw():
    shape(bg, 0, 0)
    noLoop()
 
