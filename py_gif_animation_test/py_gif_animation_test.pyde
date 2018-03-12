"""
Testing a helper for the Processing GifMaker library (https://github.com/jordanorelli)
ported to Processing 3 by 01010101 (https://github.com/01010101)
Download it from https://github.com/01010101/GifAnimation/archive/master.zip
Inspired by example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/
"""

add_library('gifAnimation')
from gif_exporter import gif_export

diameter = 1
def setup():
    size(200, 200)
    smooth()

def draw():
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter = diameter + 1
    print(frameCount)
    gif_export(GifMaker, frames=250)