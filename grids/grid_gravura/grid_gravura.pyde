"""
A funny wobbling 3D grid - by Alexandre B A Villares (abav.lugaralgum.com)
1. install Processing (processing.org)
2. install Python Mode (isntructions on py.processing.org)
3. install PeasyCam library under Sketch...>Import Libray...>Add Library...
"""
add_library('pdf')
add_library('peasycam')  # Drag the mouse to orbit!

angle = 0
RANGE = 3
NUM_BOXES = RANGE ** 3
BOXES = [()] * NUM_BOXES
S_SIZE = 10  # Controls the spacing of the grid
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
SLIDE = 5    # Changes the sliding behaviour
SPEED = 0.01 # Increments ANG
save_frame = False

def setup():
    #hint(ENABLE_DEPTH_SORT) 
    #fullScreen(1)
    size(600, 600, P3D)
    cam = PeasyCam(this, 110)
    cam.setMinimumDistance(110)
    cam.setMaximumDistance(110)
    on_grid(set_boxes, BOXES)
    strokeWeight(2)


def draw():
    global angle, save_frame

    if save_frame:
        pdf = beginRaw(PDF, "pdf_complex_out2.pdf")
        
    background(0)
    on_grid(plot_boxes, BOXES)

    if keyPressed:
        angle += SPEED

    if save_frame:
        endRaw()
        save_frame = False  
    if frameCount % 5 and frameCount < 500:
        # saveFrame("f###.tga")
        pass

def on_grid(func, L):
    n = 0
    for i in range(RANGE):
        for j in range(RANGE):
            for k in range(RANGE):
                func(i, j, k, n, L)
                n += 1

def set_boxes(x, y, z, n, L):
    r = map(x, 0, RANGE, 1, 255)
    g = map(y, 0, RANGE, 1, 255)
    b = map(z, 0, RANGE, 1, 255)
    box_size = random(B_SIZE, B_SIZE * 2)
    L[n] = (color(r, g, b), box_size)

def plot_boxes(x, y, z, n, L):
    box_color, box_size = L[n]
    noFill()
    #noStroke()    
    stroke(255)
    with pushMatrix():
        translate(x * S_SIZE * sin(angle + x * SLIDE),
                  y * S_SIZE * sin(angle + y * SLIDE),
                  z * S_SIZE * sin(angle + z * SLIDE)
                  )
        box(box_size)


def keyPressed():
    global save_frame
    if key == "s":
        save_frame = True
