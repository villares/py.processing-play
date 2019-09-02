""" CEL_SIZE, HALF_CEL = 50, 25
ANG = 0

def setup():
    global ROWS, COLS  # filas e colunas
    size(400, 400)
    ROWS, COLS = height // CEL_SIZE, width // CEL_SIZE
    rectMode(CENTER)
    frameRate(10)
    colorMode(HSB)
    noStroke()

def draw():
    global ANG
    background(0)
    for r in range(ROWS):
        for c in range(COLS):
            with pushMatrix():
                translate(HALF_CEL + c * CEL_SIZE,
                          HALF_CEL + r * CEL_SIZE)
                if int(random(2)):
                    rotate(ANG / 3)
                else:
                    rotate(ANG / 2)
                fill((ANG * (r + 1) * (c + 1)) % 255,
                     255, 255, 128)
                rect(0, 0, 100 * sin(ANG / 5),
                           100 * cos(ANG / 5))
                ANG += 0.0015

    if frameCount < 1000:
        print frameCount
        # saveFrame("###.png")
         """