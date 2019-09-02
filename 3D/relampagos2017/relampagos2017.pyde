"""
Código para fazer o convite da Noite de Processing de novembro de 2017
(c) Alexandre B A Villares (abav.lugaralgum.com)
Código: GPL v3 (mas a atribuição é apreciada)
Template do Convite / imagem de fundo: CC-BY-NC-SA
1. instale Processing (processing.org)
2. instale o Modo Python (Menu de modos, canto superior direito do IDE)
3. Instale PeasyCam library under Sketch...>Import Libray...>Add Library...
"""
add_library('pdf')
add_library('peasycam')  # Permite orbitar o 3D com o arrastar do mouse

ANG = 0
RANGE = 9
NUM_BOXES = RANGE * RANGE * RANGE * 2
BOXES = [()] * NUM_BOXES
S_SIZE = 5  # Controla o espaçamento da grade
B_SIZE = 5   # B_SIZE <= box_size < B_SIZE * 2
SLIDE = 5    # Deslizamento em ondas dos blocos
SPEED = 0.01  # Velocidade dos ciclos

def setup():
    global fundo
    fundo = loadImage("fundo22.png")
    size(600, 600, P3D)
    cam = PeasyCam(this, 190)
    cam.setMinimumDistance(190)
    cam.setMaximumDistance(190)
    on_grid(set_boxes, BOXES)


def draw():
    global ANG

    background(fundo)
    translate(0, -25, 0)
    on_grid(plot_boxes, BOXES)

    ANG += SPEED

    if not frameCount % 3 and degrees(ANG) < 360:
        # saveFrame("f###.png") # descomente esta linha para salvar frames!
        println((frameCount, degrees(ANG)))


def on_grid(func, L):
    n = 0
    for i in range(RANGE * 2):
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
    stroke(box_color)
    with pushMatrix():
        translate(x * S_SIZE * sin(ANG + x * SLIDE),
                  y * S_SIZE * sin(ANG + y * SLIDE),
                  z * S_SIZE * sin(ANG + z * SLIDE))
        box(box_size)