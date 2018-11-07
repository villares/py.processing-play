def setup():
    circle_arc(5, 5, 25, 0, HALF_PI)
    half_circle(60, 5, 25, 0)
    quarter_circle(95, 95, 25, 2)

def circle_arc(x, y, radius, start_ang, sweep_ang):
    arc(x, y, radius * 2, radius * 2, start_ang, start_ang + sweep_ang)
    
def quarter_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, quadrant * HALF_PI, HALF_PI)

def half_circle(x, y, radius, quadrant):
    circle_arc(x, y, radius, quadrant * HALF_PI, PI)
    
