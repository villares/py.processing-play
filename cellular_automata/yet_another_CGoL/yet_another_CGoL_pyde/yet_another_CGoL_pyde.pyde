"""
Yet another Conway's Game of Life example - for Processing Python Mode
"""

cell_size = 10
clr = 255      # global for random cell colour
mouse_action = 0  # global for 'mouse painting'
play = False   # simulation is running

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
    println("'b' demonstrate 'blinker'")
    println("'g' demonstrate glider")
    println("'r' to randomize grid")

def draw():
    background(0)
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y = j * cell_size
            current_state = grid[i][j]
            fill(clr, 255, 255)
            if current_state:
                square(x, y, cell_size)
            if play:
                ngbs_alive = calc_ngbs_alive(i, j)
                result = rule(current_state, ngbs_alive)
                next_grid[i][j] = result
    if play:
        step()

def rule(current, ngbs):
    """ classic Conway's Game of Life rule """
    if ngbs < 2 or ngbs > 3:
        return 0  # dies / dead
    elif ngbs == 3:
        return 1  # born / alive
    else:
        return current  # stays the same (ngbs == 2)

def calc_ngbs_alive(i, j):
    NEIGHBOURS = ((-1, 00), (01, 00),  # a tuple describing the neighbourhood of a cell
                  (-1, -1), (00, -1),
                  (01, -1), (-1, 01),
                  (00, 01), (01, 01))
    alive = 0
    for iv, jv in NEIGHBOURS:
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

def step():
    global grid, next_grid
    grid = next_grid
    next_grid = empty_grid()

def keyPressed():
    global grid, play
    if key == "e":
        grid = empty_grid()
    if key == "r":
        randomize_grid()
    if key == "g":
         grid[10][10:13] = [0, 1, 0]       
         grid[11][10:13] = [0, 0, 1]       
         grid[12][10:13] = [1, 1, 1]       
    if key == "s":
         grid[10][10:13] = [0, 1, 0]       
         grid[11][10:13] = [0, 1, 0]       
         grid[12][10:13] = [0, 1, 0]               
    if key == " ":
        play = not play

def mousePressed():
    global mouse_action
    state = cell_on_mouse(-1) # invert cell state
    if state is not None:
        mouse_action = state

def mouseDragged():
    cell_on_mouse((1, 0)[mouse_action])  # apply inverted entry state

def cell_on_mouse(action=None):
    for i in range(cols):
        x = i * cell_size
        for j in range(rows):
            y = j * cell_size
            current_state = grid[i][j]
            if mouse_over(x, y):
                if action == -1:
                    grid[i][j] = (1, 0)[current_state]
                elif action is not None:
                    grid[i][j] = action

                return current_state

def mouse_over(x, y):
    return x < mouseX < x + cell_size and y < mouseY < y + cell_size
