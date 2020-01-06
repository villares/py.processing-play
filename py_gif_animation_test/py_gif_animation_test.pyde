"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

Testing a helper for the Processing GifMaker Gif Animation librarie https://github.com/extrapixel/gif-animation/tree/3.0
Download from https://github.com/villares/processing-play/blob/master/export_GIF/unzip_and_move_to_libraries_GifAnimation.zip
This helper was inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/
"""

# add the following 2 lines
add_library('gifAnimation')
from gif_exporter import gif_export

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
