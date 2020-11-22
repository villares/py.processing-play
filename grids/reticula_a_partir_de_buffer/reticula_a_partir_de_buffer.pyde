"""
 Retícula de bolinhas brancas a partir de imagem
 Aperte 'g' para gravar um PDF na pasta do sketch
"""
add_library('pdf')
tam_celula = 4  # tamanho das células da grade
gravarPDF = False

def setup():
    global colunas, filas, img
    size(600, 400)
    noStroke()
    smooth()
    rectMode(CENTER)
    # print PFont.list()
    f = createFont("Tomorrow Bold", 80)
    colunas = int(width / tam_celula)
    filas = int(height / tam_celula)
    # Começa a captura
    img = createGraphics(600, 400)
    img.beginDraw()
    img.background(100)
    img.textFont(f)
    img.textAlign(CENTER, CENTER)
    img.textSize(100)
    img.text("Hello", width / 3, height / 3)
    img.stroke(0)
    img.strokeWeight(10)
    img.circle(450, 250, 100)
    img.filter(BLUR, 2)
    img.endDraw()

def draw():
    global gravarPDF

    if gravarPDF:
        beginRecord(PDF, "Imagem.pdf")
    background(0)
    noStroke()
    img.loadPixels()
    # Loopando as colunas da grade
    for i in range(colunas):
        # Loop das filas
        for j in range(filas):
            x = i * tam_celula
            y = j * tam_celula
            loc = x + y * img.width
            cor = img.pixels[loc]
            tam = map(brightness(cor), 0, 255, 0, tam_celula - 1)
            colorMode(HSB)
            fill(255)
            ellipse(x + tam_celula / 2, y + tam_celula / 2, tam, tam)
         # fim fo loop das filas
     # fim do loop das colunas
    if (gravarPDF):
        endRecord()
        println('gravado arquivo imagem.pdf')
        gravarPDF = False
        exit()


def keyPressed(self):
    global gravarPDF
    if key == 'g':
        gravarPDF = True
