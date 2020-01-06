"""
Alexandre B A Villares http://abav.lugaralgum.com - GPL v3 

A helper for the Processing gifAnimation library https://github.com/extrapixel/gif-animation/tree/3.0
This helper was inspired by an example by Art Simon https://github.com/APCSPrinciples/AnimatedGIF/
Download github.com/extrapixel/gif-animation/archive/3.0.zip unzip and copy into your libraries folder
user/sketchbook/libraries or user/Documents/Processing/libraries depending on your platform

# add at the start of your sketch:
  add_library('gifAnimation')
  from gif_exporter import gif_export
# add at the end of draw():
  gif_export(GifMaker, "filename")
"""

def gif_export(GifMaker,             # gets a reference to the library
               filename="exported",  # .gif will be added
               repeat=0,             # 0 makes it an "endless" animation
               quality=255,          # quality range 0 - 255
               delay=170,            # this is quick
               frames=0,             # 0 will stop only if 'e' key pressed
               finish=False):        # force stop
    global gifExporter
    try:
        gifExporter
    except NameError:
        gifExporter = GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)
        gifExporter.setQuality(quality)
        gifExporter.setDelay(delay)
        print("gif recording started")

    gifExporter.addFrame()

    if frames == 0:
       if keyPressed and key=='e':
           finish = True
    elif frameCount >= frames:
        finish = True
                
    if finish:
        gifExporter.finish()
        print("gif saved, exit")
        exit()
