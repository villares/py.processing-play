# https://github.com/processing/processing/wiki/Changes-in-3.0

def setup():
  size(400, 400);
  this.surface.setResizable(True)

def draw() :
  background(255);
  line(100, 100, width-100, height-100)

def keyPressed():
  this.surface.setSize(int(random(200, 500)),
                       int(random(200, 500))
                       )
