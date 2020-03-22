grid_size = 16
cell_list = [0] * grid_size * grid_size

def setup():
    global cell_size
    size(500, 500)
    cell_size = width / grid_size
    for i, cell in enumerate(cell_list):
        cell_color = color(random(256))
        cell_list[i] = cell_color

def draw():
    """  """
    for x in range(grid_size):
        for y in range(grid_size):
            fill(cell_list[x + y * grid_size])
            rect(x * cell_size, y * cell_size,
                 cell_size, cell_size)
