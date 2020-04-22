def setup():
    size(400, 400)

    pontos_shape = [(20, 20), (330, 50), (300, 370)]
    pontos_furo = [(290, 300), (300, 60), (100, 40)]

    poly(pontos_shape, [pontos_furo])
    # poly(pontos_shape, pontos_furo)  # tabém funciona

    saveFrame('contour_furo.png')

def poly(points, holes=None, closed=True):
    """
    Aceita como pontos sequencias de tuplas, lista ou vetores com (x, y) ou (x, y, z).
    Note que `holes` espera uma sequencias de sequencias ou uma única sequencia de
    pontos. Por default faz um polígono fechado.
    """

    def depth(seq):
        """
        usada para checar se temos um furo ou vários
        devolve 2 para um só furo, 3 para vários furos
        """
        if (isinstance(seq, list) or
                isinstance(seq, tuple) or
                isinstance(seq, PVector)):
            return 1 + max(depth(item) for item in seq)
        else:
            return 0

    beginShape()  # inicia o PShape
    for p in points:
        if len(p) == 2 or p[2] == 0:
            vertex(p[0], p[1])
        else:
            vertex(*p)  # desempacota pontos em 3d
    holes = holes or []  # equivale a: holes if holes else []
    elif depth(holes) == 2:  # sequência única de pontos
        holes = (holes,)     # envolve em um tupla
    for hole in holes:  # para cada furo
        beginContour()  # inicia o furo
        for p in hole:
            if len(p) == 2 or p[2] == 0:
                vertex(p[0], p[1])
            else:
                vertex(*p)
        endContour()  # final e um furo
    # encerra o PShape
    if closed:
        endShape(CLOSE)
    else:
        endShape()
