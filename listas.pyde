
lista_frutas = ["abacate",u"maçã","banana"]
tupla = (10, 50)
conjuto_set = {"abacate",u"maçã","banana"}
lista_de_tuplas = [(10,50),(40,50),(40,40)]

def setup():
    size(600,600)
    textSize(20)
    
def draw():
    x = 100
    for fruta in lista_frutas:
        text(fruta, x, 100)
        x = x+100
    