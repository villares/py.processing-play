"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

Testing the Processing GifMaker Gif Animation library github.com/extrapixel/gif-animation/tree/3.0
Download the library from:
https://github.com/extrapixel/gif-animation/archive/3.0.zip
Download the gif_export.py helper from:
https://github.com/villares/py.processing-play/blob/master/py_gif_animation_test/gif_export.py
Read the comments inside gif_export.py!
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
