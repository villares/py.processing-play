"""
A funny wobbling 3D grid - by Alexandre B A Villares (abav.lugaralgum.com)
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""

add_library('peasycam')  # Drag the mouse to orbit!

ANG = 0
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
B_RANGE = 5  # number_of_boxes = (B_RANGE * 2 - 1) ** 3
S_SIZE = 10  # Controls the spacing of the grid
SLIDE = 5    # Changes the sliding behaviour
SPEED = 0.01 # Increments ANG

def setup():
    global cam, colors_and_sizes
    size(600, 600, P3D)
    cam = PeasyCam(this, 200)
    cam.setMinimumDistance(200)
    cam.setMaximumDistance(200)
    colors_and_sizes = my_grid()

def draw():
    global ANG
    background(0)
    my_grid(colors_and_sizes)
    ANG += SPEED

def my_grid(L=None):
    new_L = []
    c = 0
    for i in range(-B_RANGE, B_RANGE):
        for j in range(-B_RANGE, B_RANGE):
            for k in range(-B_RANGE, B_RANGE):
                if L:
                    box_color, box_size = L[c]
                    fill(box_color)
                    my_box(i * S_SIZE * sin(ANG + i * SLIDE),
                           j * S_SIZE * sin(ANG + j * SLIDE),
                           k * S_SIZE * sin(ANG + k * SLIDE),
                           box_size)
                else:
                    r, g, b = 150 + i * 20, 150 + j * 20, 150 + k * 20
                    box_size = B_SIZE + random(B_SIZE)
                    new_L.append((color(r, g, b), box_size))
                c += 1
    return new_L

def my_box(x, y, z, s):
    with pushMatrix():
        translate(x, y, z)
        box(s)