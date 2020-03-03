"""
Minimal SVG Export test for Processing Python Mode
"""

add_library('svg')
 
def setup():
    size(400, 400)
    # PGraphics pgDrawing
    pgDrawing = createGraphics(400, 400, SVG, "test.svg")
    beginRecord(pgDrawing)
    background(255)
    stroke(0)
    strokeWeight(4)
    rect(10, 10, 70, 50, 10)
    endRecord()

def draw():
    noLoop()
 
