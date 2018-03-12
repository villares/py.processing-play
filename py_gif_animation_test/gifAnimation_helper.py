def gifExport(GifMaker, filename="exported", frames=0, repeat=0, quality=255, delay=17):
    """
    Be careful! frames=0 will stop the sketch on keyPressed or frameCount >= 100000... 
    """
    if frameCount == 1:
        global gifExporter
        gifExporter = GifMaker(this, filename + ".gif")
        gifExporter.setRepeat(repeat)  # 0 makes it an "endless" animation
        gifExporter.setQuality(quality)  # quality range 0 - 255
        gifExporter.setDelay(delay)
    gifExporter.addFrame()
        
    if (frames == 0 and keyPressed or frameCount >= 100000) or (frames != 0 and frameCount >= frames):
        gifExporter.finish()
        print("gif saved")
        exit()
 
