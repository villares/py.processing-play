"""
Exemplo de Perlin Noise em três dimensões 
"""

perlinScale = 0.1
z = 0

def setup():
    size(500, 500)  # define o tamanho da tela em pixels. Largura X Altura
    noStroke()
    colorMode(HSB)

def draw():
    background(0)
    cols = 50
    tam = width / cols
    for x in range(cols):
        for y in range(cols):
            n = noise((mouseX + x) * perlinScale, (mouseY + y) * perlinScale, z * perlinScale)
            fill(240 * n, 255, 255)
            ellipse(tam / 2 + x * tam, tam / 2 + y * tam,
                    tam - tam * n, tam - tam * n)
            
def keyPressed():
    global z
    if keyCode == UP:
        z +=1
    if keyCode == DOWN:
        z -=1
