""" Alexandre B A Villares [abav.lugaralgum.com]
    Exemplo 'Hello World' para Processing Python Mode
    Hello Garoa :-) Visite um hackerspace!
    Garoa Hacker Clube [garoa.net.br]
"""

def setup():     # setup()roda uma vez só no começo
  size(400,400)         # área de desenho
  rectMode(CENTER)      # retângulos pelo centro
  background(0,255,0)   # fundo verde (r, g, b)
  
def draw():     # draw() é o laço principal, fica repetindo
   if mousePressed:     # se o mouse pressionado
        fill(random(255),128)    # sorteia cinza translúcido
        tamanho = random (10,20) # sorteia um tamanho
        rect(mouseX, mouseY, tamanho, tamanho) # desenha
