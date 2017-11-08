"""
A funny wobbling 3D grid - by Alexandre B A Villares (abav.lugaralgum.com)
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""

add_library('peasycam')  # Drag the mouse to orbit!

ANG = 0
B_SIZE = 5    # B_SIZE < box size < B_SIZE * 2
SQ_NUM = 5    # (SQ_NUM * 2 - 1) ** 3 is the number of boxes
SQ_SIZE = 10  # Controls the maximum size of the grid
SLIDE = 5     # Changes the sliding behavior
SPEED = 0.01  # Increments ANG

def setup():
    global cam, cores_e_tamanhos
    size(600, 600, P3D)
    cam = PeasyCam(this, 200)
    cam.setMinimumDistance(200)
    cam.setMaximumDistance(200)
    cores_e_tamanhos = my_grid()

def draw():
    global ANG
    background(0)
    # translate(width/2, height/2)
    my_grid(cores_e_tamanhos)
    ANG += SPEED

def my_grid(L=None):
    new_L = []
    c = 0
    for i in range(-SQ_NUM, SQ_NUM):
        for j in range(-SQ_NUM, SQ_NUM):
            for k in range(-SQ_NUM, SQ_NUM):
                if L:
                    cor, tamanho = L[c]
                    fill(cor)
                    my_box(i * SQ_SIZE * sin(ANG + i * SLIDE),
                           j * SQ_SIZE * sin(ANG + j * SLIDE),
                           k * SQ_SIZE * sin(ANG + k * SLIDE),
                           tamanho)
                else:
                    new_L.append((color(128 + i * 12, 128 + j * 12, 128 + k * 12),
                                  B_SIZE + random(B_SIZE)))
                c += 1
    return new_L

def my_box(x, y, z, s):
    with pushMatrix():
        translate(x, y, z)
        box(s)
