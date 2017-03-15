""" Exemplo de uso da Biblioteca PeasyCam - documentaço em http://mrfeinberg.com/peasycam/
    No menu do IDE Processing: Sketch > Import Library... > Add Library.. > [search for PeasyCam & install]
    depois Import Library... > PeasyCam
    - Clique e arraste o mouse (mouseDragged) para orbitar
    - Scroll Wheel = Zoom
    - Command = Translate
"""
add_library('peasycam')

def setup():
    global camera
    size(200, 200, P3D)       # note o setup do canvas 3D
    camera = PeasyCam(this, 100)
    camera.setMinimumDistance(50)
    camera.setMaximumDistance(500)

def draw():
    rotateX(-.5)
    rotateY(-.5)
    background(0)
    fill(255, 0, 0)
    box(30)
    with pushMatrix():
        translate(0, 0, 20)
        fill(0, 0, 255)
        box(5)
    camera.beginHUD() # para desenhar relativo ao ponto de vista da câmera
    fill(255)
    rect(30,30,30,30)
    camera.endHUD()  # sempre!

        
