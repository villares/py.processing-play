""" Exemplo de uso da Biblioteca PeasyCam criada por Jonathan Feinberg
    * documentação em http://mrfeinberg.com/peasycam/
    No menu do IDE Processing: Sketch > Import Library... > Add Library.. > [search for PeasyCam & install]
    depois Import Library... > PeasyCam
    Este exemplo mostra como realocar o arraste do mouse e do botão da direita
    - Clique e arraste o botão central (rodinha) para orbitar
    - Botão da direita = Pan/Translate
    - Rodinha/mouse wheel = Zoom
    - Tecla R - reset da câmera
    - Tecla S - salva um estado
    - Tecla L - carrega o estado salvo
"""

add_library('peasycam') # import peasy.*
saved_cam_state = None
    
def setup():
    global cam
    size(200, 200, P3D)
    cam = PeasyCam(this, 100)
    cam.setMinimumDistance(50)
    cam.setMaximumDistance(500)
    # Reassign some drag handlers    
    orbitDH = cam.getRotateDragHandler()  # get the rotate Handler
    cam.setCenterDragHandler(orbitDH)     # set it to the Center/Wheel click/drag
    panDH = cam.getPanDragHandler()       # get the rotate Handler
    cam.setRightDragHandler(panDH)        # set left-button mouse drag
    cam.setLeftDragHandler(None)          # disable the right-drag

def draw():
    background(0)
    fill(255, 0, 0)
    box(30)
    pushMatrix()
    translate(0, 0, 20)
    fill(0, 0, 255)
    box(5)
    popMatrix()

def keyPressed():
    global saved_cam_state
    if key == 'r' or key == 'R': 
        cam.reset()    # reseta o estado original da câmera
    
    if key == 's' or key == 'S':
        saved_cam_state = cam.getState()    # salva estado da câmera
     
    if key == 'l' or key == 'L':
        if saved_cam_state: cam.setState(saved_cam_state)  # carrega o estado previamente salvo    
