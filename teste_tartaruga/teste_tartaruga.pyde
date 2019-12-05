from tartaruga import *

size(300, 300)
inicie_tartaruga()
suba_caneta()
ande(-50)

def pentagono(t):
    baixe_caneta()
    for i in range(5):
        ande(t)
        vire(72)
    suba_caneta()

for i in range(5):
    ande(90)
    vire(72)
    pentagono(30)
