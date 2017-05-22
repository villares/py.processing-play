""" Click on the sketch to pause and restart """

paused = False

def setup():
  size (100, 100)

def draw():
  background(0)
  text(str(frameCount), 5, 15)

def mouseClicked():
  global paused
  paused = not paused
  if paused:
    noLoop()
  else:
    loop()
