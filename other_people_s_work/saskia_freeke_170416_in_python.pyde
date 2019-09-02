"""
Ported to Processing Python Mode 
from Geometric Shapes / 170416 by Saskia Freeke 
https://www.openprocessing.org/sketch/421090
CC BY-SA https://creativecommons.org/licenses/by-sa/3.0/
"""

maxFrameCount = 150.0  # needs to be a float
a = 106

def setup():
    size(540, 540, P2D)
    noFill()

def draw():
    background('#1F1F1F')
    with pushMatrix():
        translate(width / 2, height / 2)
        t = frameCount / maxFrameCount
        theta = TWO_PI * t
        for x in range(-250, 251, 50):
            for y in range(-250, 251, 50):
                offSet = (x + y) * a
                sz2 = map(sin(-theta + offSet), -1, 1, 0, 35)
                strokeWeight(2)
                if (x + y) % 100 == 0:
                    stroke('#FFCDA5')
                    shape(x, y, 10, sz2)
                else:
                    stroke('#9A5584')
                    shape(x, y, 10, sz2)

def shape(xPos, yPos, pOne, pTwo):
    with pushMatrix():
        translate(xPos, yPos)
        rotate(radians(45))
        beginShape()
        vertex(-pOne, -pOne)
        vertex(-pOne, -pTwo)
        vertex(pOne, -pTwo)
        vertex(pOne, -pOne)
        vertex(pTwo, -pOne)
        vertex(pTwo, pOne)
        vertex(pOne, pOne)
        vertex(pOne, pTwo)
        vertex(-pOne, pTwo)
        vertex(-pOne, pOne)
        vertex(-pTwo, pOne)
        vertex(-pTwo, -pOne)
        endShape(CLOSE)
