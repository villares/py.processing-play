# Desenhos simétricos - 2019 Alexandre Villares
# Para Processing modo Python
# Como instalar o Processing em casa:
# https://abav.lugaralgum.com/como-instalar-o-processing-modo-python/   
# Sob licença GPL v3.0

add_library('pdf')

polys = []
current_poly = []
divisoes = 5
salvar_pdf = False
espelhar = True

def setup():
    size(700, 700)
    strokeJoin(ROUND)

def draw():
    if salvar_pdf:
        beginRecord(PDF, "####.pdf")

    mh, mv = width / 2, height / 2
    translate(mh, mv)
    background(240, 240, 200) 
    
    angulo = radians(360. / divisoes)
    fill(0, 0, 200)
    noStroke()
    for num in range(divisoes):
        rotate(angulo)
        for poly in polys:
            draw_poly(poly)
            if espelhar:
                scale(-1, 1)
                draw_poly(poly)
                scale(-1, 1)
    
    if salvar_pdf:
        endRecord()
        global salvar_pdf
        salvar_pdf = False

    if current_poly:
        noFill()
        stroke(0)
        for num in range(divisoes):
            rotate(angulo)
            draw_poly(current_poly + [(mouseX, mouseY)])
            if espelhar:
                scale(-1, 1)
                draw_poly(current_poly + [(mouseX, mouseY)])
                scale(-1, 1)
    
def draw_poly(poly):
    pushMatrix()
    translate(-width / 2, -height / 2)
    beginShape()
    for p in poly:
        vertex(p[0], p[1])
    endShape(CLOSE)
    popMatrix()

def mousePressed():  # def mouseDragged():
    if mouseButton == LEFT:
        current_poly.append((mouseX, mouseY))    
    if mouseButton == RIGHT and len(current_poly) > 1:
        polys.append(current_poly + [(mouseX, mouseY)])
        current_poly[:] = []

def keyPressed():
    global salvar_pdf, divisoes, espelhar
    if key == "a":
        polys[:] = [[]]  # esvazia lista de polys
    if key == "g":
        saveFrame("#####.png")
        print("salvando PNG")
    if key == "p":
        salvar_pdf = True
        print("salvando PDF")
    if key == BACKSPACE:
        if current_poly:
            current_poly.pop()
        elif polys:
            polys.pop()
    if key == "-" and divisoes > 2:
        divisoes -= 1
    if key == "+" or key == "=":
        divisoes += 1        
    if key == "e":
        espelhar = not espelhar
        
