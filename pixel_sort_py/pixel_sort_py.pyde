
thread_ongoing = False
sort_by = None

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
    global thread_ongoing, sort_by
    
    options = {
        "w" : brightness,
        "r" : red,
        "g" : green,
        "b" : blue,
        "h" : hue,
        "s" : saturation,
        "c" : lambda pix: pix,
        }
    
    if thread_ongoing:
        thread_ongoing = False
    else:
        sort_by = options.get(key)
        if sort_by:
            thread_ongoing = True
            thread("sort_it")
        else:
            thread_ongoing = False

    
def sort_it():
    print("sort_it() started!")
    global thread_ongoing
    if thread_ongoing:
        print(key)
        for i in range(len(img.pixels)):
            record_value = -1000000000
            selected_pixel = i
            for j in range (i,  len(img.pixels)):
                pix = img.pixels[j]
                if sort_by:
                    value = sort_by(pix)                
                    if value > record_value:
                        selected_pixel = j
                        record_value = value
            # troca o pixel em selected_pixel com o i
            temp = img.pixels[i]
            img.pixels[i] = img.pixels[selected_pixel]
            img.pixels[selected_pixel] = temp
            img.updatePixels()
            redraw()
        println("done!")
        thread_ongoing = False
    print(thread_ongoing)
    println("end!")
