def setup():
    circle_arc(50, 50, 25, 0, HALF_PI)
    quarter_circle(50, 50, 25, 2)
    half_circle(50, 75, 25, 0)

def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
    
def quarter_circle(x, y, radius, quadrant):
    circle_arc(50, 50, 25, quadrant * HALF_PI, HALF_PI)

def half_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, quadrant * HALF_PI, PI)
