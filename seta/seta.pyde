import random as rnd

LISTA = []
MARGIN = 25

def setup():
    size(500, 500)
    background(200)
    noFill()
    smooth(12)
    LISTA[:] = []
    for _ in range(20):
        LISTA.append((
            random(MARGIN, width - MARGIN),  # x
            random(MARGIN, height - MARGIN),  # y
            rnd.choice([10, 20, 30]),  # size
            rnd.choice([2, 3, 5]),  # strokeW
            rnd.choice([True, False]),  # arrow
            list()  # other nodes
        ))
    for node in LISTA:
        random_node = rnd.choice(LISTA)
        if random_node != node:
            node[-1].append(random_node)


def seta(x1, y1, x2, y2, shorter=12, head=12):
    """ draws an arrow """
    L = dist(x1, y1, x2, y2)
    with pushMatrix():
        translate(x2, y2)
        angle = atan2(x1 - x2, y2 - y1)
        rotate(angle)
        offset = -shorter * .6
        line(0, offset, 0, -(L + offset))
        line(0, offset, -head / 3, -head + offset)
        line(0, offset, head / 3, -head + offset)

def draw():
    for x, y, s, w, arrow, sub_lista in LISTA:
        strokeWeight(w)
        for n in sub_lista:
            if arrow:
                stroke(0)
                seta(x, y, n[0], n[1], s, w*5)
            else:
                stroke(255)
                line(x, y, n[0], n[1])
        ellipse(x, y, s, s)
