# Desenhos simétricos - 2019-2022 Alexandre Villares - code under GPL v3.0
# Using py5.ixora.io (Processing + Python) and shapely
# you'll need to install py5 and shapely

from shapely.geometry import Polygon, MultiPolygon
from shapely.geos import TopologicalError
from shapely.ops import unary_union

segments = []      # press "a" to erase all segments
next_seg_preview = []  
seg_limit = 8
start_w = 10       # segment (starting) width
end_w = 10         # ... ending width (for trapezoidal segs)
divisions = 5      # Use "+" and "-" to change
save_pdf = False   # Use "p" to save a PDF
mirror = True      # Use "m" to toggle
                   # press <backspace> to remove last segment/click
def setup():
    global mh, mv
    size(500, 500)
    mh, mv = width / 2, height / 2

def draw():
    background(0, 128, 32)  # it's better to leave the background out!

    global save_pdf
    if save_pdf:
        begin_record(PDF, "####.pdf")
   
    translate(mh, mv)
    bars = []
    for num in range(divisions):
        angle = radians(360.0 / divisions) * num
        fill(255)
        for segment in segments:
            x1, y1, x2, y2 = segment
            pts = bar_points(x1, y1, x2, y2, start_w, end_w)
            rotated_points = [rot((x, y), angle) for x, y in pts]
            bars.append(Polygon(rotated_points))
            if mirror:
                bars.append(Polygon([(x, -y) for x, y in rotated_points]))
    if len(bars) > 1:
        result = unary_union(bars)
        draw_poly(result)

    if save_pdf:
        end_record()
        save_pdf = False

    preview_bars()

def draw_poly(poly):
    if isinstance(poly, MultiPolygon):
        for p in poly.geoms:
            draw_poly(p)
    elif isinstance(poly, Polygon):
        begin_shape()
        for x, y in poly.exterior.coords:        
            vertex(x, y)
        for hole in poly.interiors:
            begin_contour()
            for x, y in hole.coords:        
                vertex(x, y)
            end_contour()
        end_shape(CLOSE)
    else:
        begin_shape()  
        for x, y in poly:
            vertex(x, y)
        end_shape(CLOSE)      


def mouse_pressed(): 
    if len(segments) < seg_limit:
        if next_seg_preview:
            px, py = next_seg_preview
            segments.append((px, py, mouse_x - mh, mouse_y - mv))
        if mouse_button == LEFT:
            next_seg_preview[:] = mouse_x - mh, mouse_y - mv
        elif mouse_button == RIGHT:
            next_seg_preview[:] = []

def key_pressed():
    global save_pdf, divisions, mirror
    if key == "m":
        mirror = not mirror
    if key == "a":
        segments[:] = []    # erase all segments
        next_seg_preview[:] = []
    if key == "g":
        saveFrame("#####.png")
        print("saving PNG")
    if key == "p":
        save_pdf = True
        print("saving PDF")
    if key == BACKSPACE and segments: 
        segments.pop()      # remove last segment
    if key == "-" and divisions > 2:
        divisions -= 1
    if key == "+" or key == "=" and divisions < 12:
        divisions += 1        
   
def preview_bars():
    if next_seg_preview and len(segments) < seg_limit:
        p1x, p1y = next_seg_preview
        p2x, p2y = mouse_x - mh, mouse_y - mv
        push()        
        for num in range(divisions):
            rotate(radians(360 / divisions))
            fill(255, 100)
            draw_poly(bar_points(p1x, p1y, p2x, p2y, start_w, end_w))
            if mirror:
                draw_poly(bar_points(p1x, -p1y, p2x, -p2y, start_w, end_w))    
        pop()  

def bar_points(p1x, p1y, p2x, p2y, w1, w2=None, o=0):
    """ 
    trapezoid, draws a rotated quad with axis
    starting at (p1x, p1y) ending at (p2x, p2y) where
    w1 and w2 are the starting and ending side widths.
    """
    if w2 is None:
        w2 = w1
    d = dist(p1x, p1y, p2x, p2y)
    angle = atan2(p1x - p2x, p2y - p1y)  + HALF_PI
    unrotated_points = (
        (p1x - o, p1y - w1 / 2),
        (p1x - o, p1y + w1 / 2),
        (p1x + d + o, p1y + w2 / 2),
        (p1x + d + o, p1y - w2 / 2)
        )
    return [rot(pt, angle, center=(p1x, p1y)) 
              for pt in unrotated_points]

def rot(pt, angle, center=None):
    xp, yp = pt
    x0, y0 = center or (0, 0)
    x, y = xp - x0, yp - y0  # translate to origin
    xr = x * cos(angle) - y * sin(angle)
    yr = y * cos(angle) + x * sin(angle)
    return (xr + x0, yr + y0)
