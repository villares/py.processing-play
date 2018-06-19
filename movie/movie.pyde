add_library('video')

def setup():
    global movie
    size(640, 360)
    background(0)
    
    movie = Movie(this, "transit.mov")
    movie.loop()
    
def movieEvent(m):
    m.read()
    
def draw():
    image(movie, 0,0,width,height)
