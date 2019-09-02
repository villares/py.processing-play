"""
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""

add_library('peasycam')  # Drag the mouse to orbit!
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, porta_serial in enumerate(Arduino.list()):  # Enumera portas seriais
    println(str(num)+":"+porta_serial)               # Mostra no console
NUM_PORTA = 3  # Precisa mudar! Leia a lista no console para descobrir
arduino = Arduino(this, Arduino.list()[NUM_PORTA], 57600)

ANG = 0
HALF_RANGE = 5  
NUM_BOXES = (HALF_RANGE * 2) ** 3
BOXES = [()] * NUM_BOXES
S_SIZE = 10  # Controls the spacing of the grid
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
SLIDE = 5    # Changes the sliding behaviour
SPEED = 0.01 # Increments ANG

def setup():
    size(600, 600, P3D)
    cam = PeasyCam(this, 200)
    cam.setMinimumDistance(200)
    cam.setMaximumDistance(200)
    on_grid(init_boxes, BOXES)

def draw():
    global ANG, X, Y, Z
    background(0)
    X = arduino.analogRead(0)/103 - 5 # pino A5 (analógico)
    Y = arduino.analogRead(1)/103 - 5
    Z  = arduino.analogRead(2)/103 - 5
    on_grid(input_boxes, BOXES)
    on_grid(plot_boxes, BOXES)
    ANG += SPEED

def on_grid(func, L):
    n = 0
    for i in range(-HALF_RANGE, HALF_RANGE):
        for j in range(-HALF_RANGE, HALF_RANGE):
            for k in range(-HALF_RANGE, HALF_RANGE):
                func(i, j, k, n, L)
                n += 1

def init_boxes(x, y, z, n, L):
    r, g, b = 150 + x * 20, 150 + y * 20, 150 + z * 20
    box_size = random(B_SIZE, B_SIZE * 2)
    L[n] = (color(r, g, b), 0)
    
def input_boxes(x, y, z, n, L):
    box_size = random(B_SIZE, B_SIZE * 2)
    println((X, Y, Z))
    if (x == X and y == Y and z == Z):
        L[n] = (L[n][0], box_size)

def plot_boxes(x, y, z, n, L):
    box_color, box_size = L[n]
    fill(box_color)
    with pushMatrix():
        translate(x * S_SIZE,
                  y * S_SIZE,
                  z * S_SIZE)
        box(box_size)
        
def keyPressed():
    on_grid(init_boxes, BOXES)