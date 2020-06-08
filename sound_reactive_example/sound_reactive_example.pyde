add_library('sound') # aviso de que vai usar o microfone

def setup():
    size(600, 600)  
    global input, loudness, waveform, samples
    source = AudioIn(this, 0)
    source.start()
    loudness = Amplitude(this)
    loudness.input(source)
    samples = 60
    waveform = Waveform(this, samples)
    waveform.input(source)

def draw():
    background(0) 
    volume = loudness.analyze()
    for i, w in enumerate(waveform.analyze()):
        fill(128)
        rect(i * 10, 300, 10, 300 * w)        
    s = int(map(volume, 0, 0.5, 10, 100))
    fill(255)
    ellipse(300, 300, s, s)
