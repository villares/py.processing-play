def setup():
    size(400, 400)
    
def draw():
    background(200)    
    noFill()
    theta = map(mouseX, 0, width, QUARTER_PI, TWO_PI)
    points = map(mouseY, 0, height, 2, 36)
    stroke(0)
    poly_arc(200, 200, 180, 0, theta, points)    
    stroke(255, 0, 0)
    circle_arc(200, 200, 180, 0, theta)    
    
def poly_arc(x, y, radius, start_ang, sweep_ang, num_points=2):
    angle = sweep_ang / int(num_points)
    a = start_ang
    with beginShape(): 
        while a <= start_ang + sweep_ang:
            sx = x + cos(a) * radius
            sy = y + sin(a) * radius
            vertex(sx, sy)
            a += angle
            
def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
