add_library('peasycam')

ANG = 0
B_SIZE = 5
SQ_NUM = 5
SQ_SIZE = 10
SLIDE = 5

def setup():
    global cam, cores_e_tamanhos
    size(600, 600, P3D)
    cam = PeasyCam(this, 200)
    cam.setMinimumDistance(200)
    cam.setMaximumDistance(200)
    cores_e_tamanhos = my_grid()

def draw():
    global ANG
    ANG += 0.01
    background(0)
    # translate(width/2, height/2)
    my_grid(cores_e_tamanhos, True)
    
def my_grid(L = None, plot = False):
    if not L: 
        L = []
    c = 0
    for i in range(-SQ_NUM, SQ_NUM):
        for j in range (-SQ_NUM, SQ_NUM):
            for k in range (-SQ_NUM, SQ_NUM):
                if plot:
                    cor, tamanho = L[c]
                    fill(cor)
                    my_box(i * SQ_SIZE*sin(ANG+i*SLIDE),
                           j * SQ_SIZE*sin(ANG+j*SLIDE),
                           k * SQ_SIZE*sin(ANG+k*SLIDE),
                           tamanho)
                else:
                    L.append((color(128+i*12,128+j*12,128+k*12),
                              B_SIZE + random(B_SIZE)))
                c += 1
    return L
                
def my_box(x, y, z, s):
    with pushMatrix():
        translate(x, y, z)
        box(s)