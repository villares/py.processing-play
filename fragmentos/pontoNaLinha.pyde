"""
 Code from Andreas Schlegel / http://www.sojamo.de
 posted on https://processing.org/discourse/beta/num_1247920826.html
 ported to Python Mode by Alexandre Villares
"""
def setup():
  global p1, p2, mouse
  size(400,400)
  mouse = PVector()
  p1 = PVector(100,100)
  p2 = PVector(200,200)

def draw():
  background(0)
  stroke(255)
  mouse.set(mouseX, mouseY)
  if(pointInsideLine(mouse, p1, p2, 4)==True):
     stroke(0,255,0)
  line(p1.x, p1.y,p2.x,p2.y)

def pointInsideLine(thePoint, theLineEndPoint1, theLineEndPoint2, theTolerance):
  """ 
  """                        
  dir = PVector(theLineEndPoint2.x, theLineEndPoint2.y)
  dir.sub(theLineEndPoint1)
  diff = PVector(thePoint.x, thePoint.y)
  diff.sub(theLineEndPoint1)
  # inside distance determines the weighting 
  # between linePoint1 and linePoint2 
  insideDistance = diff.dot(dir) / dir.dot(dir)
  if(insideDistance>0 and insideDistance<1):
     # thePois inside/close to 
     # the line if insideDistance>0 or <1            
     closest = PVector(theLineEndPoint1.x, theLineEndPoint1.y)
     dir.mult(insideDistance)
     closest.add(dir)
     d = PVector(thePoint.x, thePoint.y)
     d.sub(closest)
\    distsqr = d.dot(d)
     # check the distance of thePoto the line against our tolerance. 
     return (distsqr < pow(theTolerance,2)) 
  return False
