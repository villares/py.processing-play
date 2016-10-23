lista_frutas = ["abacate",u"maçã","banana"]
tupla = (10, 50)
conjuto_set = {"abacate",u"maçã","banana"}
lista_de_tuplas = [(10,50),(40,50),(40,40)]

def setup():
    size(600,600)
    noLoop()
    textSize(20)
    
def draw():
    for i,fruta in enumerate(lista_frutas):
        text(fruta, i*100, 100)
        
