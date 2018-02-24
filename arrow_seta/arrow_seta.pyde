def arrow(x1, y1, x2, y2, shorter=0, head=None):
    """
    O código para fazer setas, dois pares (x, y),
    um parâmetro de encurtamento: shorter
    e para o tamanho da cabeça da seta: head
    """
    L = dist(x1, y1, x2, y2)
    if not head:
        head = max(L / 10, 10)
    with pushMatrix():
        translate(x1, y1)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = shorter / 2
        strokeCap(ROUND)
        line(0, L - offset, -head / 3, L - offset - head)
        line(0, L - offset, head / 3, L - offset - head)
        strokeCap(SQUARE)
        line(0, offset, 0, L - offset)

def setup():
    size(400, 400)
    noFill()
    
def draw():
    background(200)
    strokeWeight(map(mouseX, 0, width, 1, 10))
    stroke(255)
    ellipse(100, 100, 30, 30)
    ellipse(100, 300, 30, 30)
    stroke(0)
    arrow(100, 100, 100, 300, shorter=30, head=30)
    arrow(150, 100, 150, 300)
    arrow(200, 100, 200, 150)
    arrow(50, 100, 350, 300)


