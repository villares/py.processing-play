add_library('sound')

numsounds = 5

def setup():
    global sounds
    size(500, 500)
    sounds = []
    for i in range(numsounds):
        file_name = "{}.aif".format(i + 1)
        sounds.append(SoundFile(this, file_name))
    
def draw():
    background(240, 250, 250)
    
def keyPressed():
    k = int(key)
    if 0 < k < numsounds:
         sounds[k].play(1, 1.0)
