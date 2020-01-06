"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

Testing a helper for the Processing GifMaker Gif Animation library
https://github.com/extrapixel/gif-animation/tree/3.0
Download github.com/extrapixel/gif-animation/archive/3.0.zip
Read the comments inside gif_export.py
"""

# add the following 2 lines
add_library('gifAnimation')
from gif_export import gif_export

diameter = 1

def setup():
    size(200, 200)
    smooth()

def draw():
    # your animation drawing goes here
    global diameter
    ellipse(50, 50, diameter, diameter)
    diameter = diameter + 1
    print(frameCount)
    # then add this line at the end of draw()
    gif_export(GifMaker, frames=250)
