"""
 Retícula de bolinhas brancas a partir da câmera
 Aperte 'g' para gravar um PDF na pasta do sketch
"""
add_library('video')
add_library('pdf')
tam_celula = 16  # tamanho das células da grade
gravarPDF = False

def setup():
    global colunas, filas, video
    size(640, 480)
    noStroke()
    smooth()
    rectMode(CENTER)
    colunas = int(width / tam_celula)
    filas = int(height / tam_celula)
    video = Capture(this, width, height)
    # Começa a captura
    video.start()
    background(0)


def draw():
    global gravarPDF
    if video.available():
        # se foi apertado 'g'
        if gravarPDF:
            fill(0)
            rect(0, 0, width, height)
            beginRecord(PDF, "Imagem.pdf")
        background(0)
        video.read()
        video.loadPixels()
        # Loopando as colunas da grade
        for i in range(colunas):
            # Loop das filas
            for j in range(filas):
                x = i * tam_celula
                y = j * tam_celula
                loc = x + y * video.width
                cor = video.pixels[loc]
                tam = map(brightness(cor), 0, 255, 0, tam_celula - 1)
                fill(255)
                ellipse(x + tam_celula / 2, y + tam_celula / 2, tam, tam)
             # dim fo loop das filas
         # fim do loop das colunas
        if (gravarPDF):
            endRecord()
            println('gravado arquivo imagem.pdf')
            gravarPDF = False


def keyPressed(self):
    global gravarPDF
    if key == 'g':
        gravarPDF = True
