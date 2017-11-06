""" 
Requires Firmata (Arduino) to be installed on Processing
Ajust SERIAL to the USB port where your Arduino is connected
May require 'sudo chmod 666 /dev/ttyUSB0' (YMMV).
"""

# ARDUINO
add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

for num, port in enumerate(Arduino.list()):  # Serial ports
    println(str(num)+":"+port)               # on console
SERIAL = 0  # Please change if needed!

POT_1 = 5   # Pin number for 1st Pot
POT_2 = 0   # Pin number for 2nd Pot

def setup():
    colorMode(HSB)  # Not using RGB mode this time ;)
    frameRate(30)
    size(1024, 1024)  # Screen size
    global arduino
    arduino = Arduino(this, Arduino.list()[SERIAL], 57600)
    background(255)
    noStroke()

def draw():
    # background(0) 
    X = arduino.analogRead(POT_1)
    Y = arduino.analogRead(POT_2)
    fill(frameCount % 255, 200, 255)  # notice HSB mode on setup!
    ellipse(X, Y, 20, 20)
    clear_screen = keyPressed #arduino.digitalRead(2)
    if clear_screen:
        background(195, 183, 242)  # light blue