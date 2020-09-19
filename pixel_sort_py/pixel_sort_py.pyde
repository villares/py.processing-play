
sort_by = None
thread_on = False

def setup():
    global img, original
    size(1000, 500)
    original = loadImage("b.png")
    img = original.get()
    img.loadPixels()
    println("loaded " + str(len(img.pixels)))


def draw():
    scale(2.5)
    background(0)
    image(original, 0, 0)
    image(img, 200, 0)
           
def keyPressed():
    global thread_ongoing, sort_by

    options = {
        "w": brightness,
        "r": red,
        "g": green,
        "b": blue,
        "h": hue,
        "s": saturation,
        "c": lambda pix: pix,  # sort color as int
    }

    sort_by = options.get(key)
    if not thread_on:
        thread("sort_it")
        
def sort_it():
    global sort_by, thread_on
    thread_on = True
    print("sort_it() started")
    print(key)
    total = len(img.pixels)
    pxs = img.pixels
    for i in range(total):
        record_value = -10000000000000
        selected_pixel = i
        for j in range(i, total):
            pix = pxs[j]
            if sort_by:
                value = sort_by(pix)
                if value > record_value:
                    selected_pixel = j
                    record_value = value
            else:
                break
        if not sort_by:
            break
        # troca o pixel em selected_pixel com o i
        img.pixels[i], img.pixels[selected_pixel] \
            = img.pixels[selected_pixel], img.pixels[i]
        pxs = img.pixels
        img.updatePixels()

    thread_on = False
    println("sort done (or interrupted)!")
    println("sort_it() end")
    # return
