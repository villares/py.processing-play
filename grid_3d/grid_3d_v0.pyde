add_library('peasycam')

SQ_NUM = 5
SQ_SIZE = 10
B_SIZE = 5
a = 0

def setup():
    global cam, cores_e_tamanhos
    size(600, 600, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(100)
    cam.setMaximumDistance(200)
    cores_e_tamanhos = my_grid()

def draw():
    global a
    a += 0.01
    background(0)
    # translate(width/2, height/2)
    my_grid(cores_e_tamanhos, True)
    
def my_grid(L = None, plot = False):
    global a
    if not L: 
        L = []
    c = 0
    for i in range(-SQ_NUM, SQ_NUM):
        for j in range (-SQ_NUM, SQ_NUM):
            for k in range (-SQ_NUM, SQ_NUM):
                if plot:
                    cor, tamanho = L[c]
                    fill(cor)
                    my_box(i * SQ_SIZE*sin(a+i/2),
                           j * SQ_SIZE*sin(a+j/2),
                           k * SQ_SIZE*sin(a+k/2),
                           tamanho)
                else:
                    L.append((color(128+i*12,128+j*12,128+k*12),
                              5 + random(5)))
                c += 1
    return L
                
def my_box(x, y, z, s):
    with pushMatrix():
        translate(x, y, z)
        box(s)