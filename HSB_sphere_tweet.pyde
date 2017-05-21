"""
Ported from code by aBe @hamoid https://twitter.com/hamoid/status/865931219132960769
by Alexandre Villares https://twitter.com/villares https://github.com/villares
"""

from itertools import count, takewhile

def setup():
    size(600, 600, P3D)
    colorMode(HSB)    

def keyPressed():
    if key == ' ':
        background("#EAD5B3")
        translate(width/2, height/2, -212)
        rotateX(-1.8)
        rotateY(1.0)
        sz = 250
        pval = 0.0
        for A in frange(0, PI, 0.001):
            r = sin(A)
            step = TWO_PI / (1 + 1000 * r)
            for B in frange(0, TWO_PI, step): 
                vv = sin(A * 7 + sin (1+B*13))* sin(B*5+sin(2+A*11))
                val = sz + 100 * vv * vv
                h = (10 + val) % 256
                s = 127 + 80 * cos(33 + h * 0.015)
                b = 200 + 20 * (noise(sin(B*2), cos(A*2)) - 0.5) + 10*(val-pval)
                stroke (h, s, b)
                x = val * sin(A) * cos (B)
                y = val * sin (A) * sin(B)
                z = val * cos(A)
                line(0, 0, 0, x, y, z)
                pval = val

def frange(start, stop, step):
        return takewhile(lambda x: x< stop, count(start, step))

def draw():
    pass
