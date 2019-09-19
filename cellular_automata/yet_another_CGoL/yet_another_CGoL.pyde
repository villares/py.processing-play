"""
Yet another Conway's Game of Life example - for Processing Python Mode
"""

NEIGHBOURS = ((-1,  0), ( 1,  0),
              (-1, -1), ( 0, -1),
              ( 1, -1), (-1,  1),
              ( 0,  1), ( 1,  1)) 
play = False
cell_size = 10
clr = 255

def setup():
    global grid, next_grid, rows, cols
    size(800, 500)
    colorMode(HSB)
    noStroke()
    rows = height / cell_size
    cols = width / cell_size
    grid = empty_grid()
    next_grid = empty_grid()
    randomize_grid()
    println("Press 'space' to start/stop")
    println("'e' to clear all cells")
    println("'r' to randomize grid")

def draw():
    background(0)
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y  = j * cell_size
            current_state = grid[i][j]
            # fill(clr, 255, current_state * 255, 100) # translucent
            fill(clr, 255, current_state * 255)
            if current_state:
                # circle(x, y, cell_size * 2) # overlapping circles
                square(x, y, cell_size)
            if play:
                ngbs_alive = calc_ngbs_alive(i, j)
                result = rule(current_state, ngbs_alive)
                next_grid[i][j] = result  
    
    if play:
        step()

def calc_ngbs_alive(i, j):
    alive = 0
    for iv, jv  in NEIGHBOURS:
        alive += grid[(i + iv) % cols][(j + jv) % rows]
    return alive

def empty_grid():
    grid = []
    for _ in range(cols):
        grid.append([0] * rows)
    return grid

def randomize_grid():
    from random import choice
    global clr
    clr = random(255)
    for i in range(cols):
        for j in range(rows):
            grid[i][j] = choice((0, 1))

def rule(s, v):
    if v < 2 or v > 3:
        return 0
    elif v == 3:
        return 1
    else:
        return s

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def keyPressed():
    global grid
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == " ":
        global play
        play = not play
        
def mouseReleased():
    invert_on_mouse()

def mouseDragged():    
    invert_on_mouse()
    
def invert_on_mouse():    
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y  = j * cell_size
            current_state = grid[i][j]
            if mouse_over(x, y):
                grid[i][j] = (1, 0)[current_state]
                
def mouse_over(x, y):
    return x < mouseX < x + cell_size and y < mouseY < y + cell_size
