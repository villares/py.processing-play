CEL_SIZE = 50
HALF_CEL = CEL_SIZE / 2
ANG = 0

def setup():
    global ROWS, COLS # filas e colunas
    size(400, 400)
    ROWS, COLS = int(height / CEL_SIZE), int(width / CEL_SIZE)
    rectMode(CENTER)
    frameRate(10)
    # noStroke()

def draw():
    global ANG
    background(255)
    for r in range(ROWS):
        for c in range(COLS):
            with pushMatrix():
                translate(HALF_CEL + c * CEL_SIZE,
                          HALF_CEL + r * CEL_SIZE)
                if COLS-c < 4 or c == 1:
                    rotate(ANG/10)
                else: 
                    rotate(ANG/2)    
                fill(ANG*100 % 255, r * 15 % 255, c * 17 % 255, 100)
                rect(0, 0, 100 * sin(ANG/5), 100* cos(ANG/5))
                ANG += 0.001
