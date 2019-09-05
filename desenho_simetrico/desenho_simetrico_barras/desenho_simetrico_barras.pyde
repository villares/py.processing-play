# Desenhos simétricos - 2019 Alexandre Villares
# Para Processing modo Python
# Como instalar o Processing em casa:
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/   
# Sob licença GPL v3.0

add_library('pdf')

linhas = []
proximo_clique = []
limite_linhas = 8

e_inicial = 10 # espessura do traço 
e_final = 10
divisoes = 5  # inicial, muda com + e -
salvar_pdf = False
espelhar = True


def setup():
    size(500, 500)

def draw():
    global salvar_pdf
    if salvar_pdf:
        beginRecord(PDF, "####.pdf")

    stroke(255)  # traço branco
    strokeWeight(1)  # espessura do traço ("peso")
    mh, mv = width / 2, height / 2
    translate(mh, mv)
    background(0, 128, 32)  # verde (mude a sua cor!)

    for num in range(divisoes):
        rotate(radians(360. / divisoes))
        fill(255)
        for linha in linhas:
            x1, y1, x2, y2 = linha
            bar(x1 - mh, y1 - mv, x2 - mh, y2 - mv, e_inicial, e_final)
            if espelhar:
                scale(1, -1)
                bar(x1 - mh, y1 - mv, x2 - mh, y2 - mv,  e_inicial, e_final)
                scale(1, -1)
    
    if salvar_pdf:
        endRecord()
        salvar_pdf = False

    if proximo_clique and len(linhas) < limite_linhas:
        for num in range(divisoes):
            rotate(radians(360 / divisoes))
            fill(255, 100)
            bar(proximo_clique[0] - mh, proximo_clique[1] - mv,
                 mouseX - mh, mouseY - mv, e_inicial, e_final)
            if espelhar:
                scale(1, -1)
                bar(proximo_clique[0] - mh, proximo_clique[1] - mv,
                    mouseX - mh, mouseY - mv,  e_inicial, e_final)
                scale(1, -1)
    
def mousePressed():  # def mouseDragged():
    if len(linhas) < limite_linhas:
        if proximo_clique:
            px, py = proximo_clique
            linhas.append((px, py, mouseX, mouseY))
        if mouseButton == LEFT:
            proximo_clique[:] = mouseX, mouseY
        elif mouseButton == RIGHT:
            proximo_clique[:] = []
    
def keyPressed():
    global salvar_pdf, divisoes, espelhar
    if key == "e":
        espelhar = not espelhar
    if key == "a":
        linhas[:] = []  # esvazia lista de linhas
        proximo_clique[:] = []
    if key == "g":
        saveFrame("#####.png")
        print("salvando PNG")
    if key == "p":
        salvar_pdf = True
        print("salvando PDF")
    if key == BACKSPACE and linhas: # delete do mac
        linhas.pop()
    if key == "-" and divisoes > 2:
        divisoes -= 1
    if key == "+" or key == "=" and divisoes < 12:
        divisoes += 1        
   
        
def bar(p1x, p1y, p2x, p2y, w1, w2=None):
    """ 
    trapezoid
    """
    if w2 is None:
        w2 = w1
    #line(p1x, p1y, p2x, p2y)
    d = dist(p1x, p1y, p2x, p2y)
    with pushMatrix():
            translate(p1x, p1y)
            angle = atan2(p1x - p2x, p2y - p1y)  + HALF_PI
            rotate(angle)
            beginShape()  
            vertex(0, -w1 / 2)
            vertex(0, w1 / 2)
            vertex(d, w2 / 2)                
            vertex(d, -w2 / 2)
            endShape(CLOSE)    
