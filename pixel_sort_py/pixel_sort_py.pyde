
go = False
kind = ""

def setup():
    global img, original
    size(1000, 500)
    original = loadImage("b.png")
    img = original.get()
    img.loadPixels()
    println("loaded " + str(len(img.pixels)))
    noLoop()


def draw():
    scale(2.5)
    background(0)
    image(original, 0, 0)
    image(img, 200, 0)
    if not frameCount % 20:
        img.updatePixels()
        

def keyPressed():
    global go, kind
    if go:
        go = False
    else:
        go = True
        kind = key
        thread("sort_it")

    
def sort_it():
    global go
    if go:
        for i in range(len(img.pixels)):
            record_value = -1000000000
            selected_pixel = i
            for j in range (i,  len(img.pixels)):
                pix = img.pixels[j]
                value = 0
                if kind == 'b':
                    value = brightness(pix)
                elif kind == 'h':
                    value = hue(pix)
                elif kind == 's':
                    value = saturation(pix)
                elif kind == 'r':
                    value = red(pix)
                elif kind == 'g':
                    value = green(pix)
                elif kind == 'a':
                    value = blue(pix)
                elif kind == 'c':
                    value = pix
                else:
                    break
                if value > record_value:
                    selected_pixel = j
                    record_value = value

            # troca o pixel em selected_pixel com o i
            temp = img.pixels[i]
            img.pixels[i] = img.pixels[selected_pixel]
            img.pixels[selected_pixel] = temp
            img.updatePixels()
            redraw()
            print(kind)

        println("done!")
        go = False
