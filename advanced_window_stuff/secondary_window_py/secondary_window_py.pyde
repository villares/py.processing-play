
def setup():
    size(200, 300)
    second_window = OtherWindow("2nd")  
    
def draw():
    background(0)
    ellipse(mouseX, mouseY, 10, 10)


class OtherWindow(PApplet):  
        
    def __init__(self, title=""):
        switches = ('--sketch-path=' + sketchPath(), '')
        PApplet.runSketch(switches, self)  
        self.surface.setTitle(title)
        
    def settings(self):
        self.size(300, 200)
        
    def draw(self):  # este é o draw pra a segunda janela
        self.background(255)
        self.fill(0)
        self.rect(self.mouseX, self.mouseY, 10, 10)
