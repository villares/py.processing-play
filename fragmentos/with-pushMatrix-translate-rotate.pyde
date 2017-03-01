def setup():
    size(200, 200)
    rectMode(CENTER)
    
def draw():
    background(255)
    fill(100)
    rect(40, 40, 40, 40)
    with pushMatrix():
        translate(mouseX, mouseY)
        rotate(radians(frameCount))
        fill(255)
        rect(0, 0, 40, 40)
        with pushMatrix():
            translate(20, 20)
            rotate(radians(frameCount*3))
            fill(200)
            rect(0, 0, 20, 20)
 
            
