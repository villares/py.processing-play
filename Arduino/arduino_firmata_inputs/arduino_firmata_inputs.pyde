from __future__ import unicode_literals
from option_pane import option_pane

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

port_list = [str(num) + ": " + porta_serial for num, porta_serial
             in enumerate(Arduino.list())]

def setup():
    global arduino
    size(470, 280)
    selection = option_pane("Is your Arduino board connected?",
                            "Select the USB port:",
                            port_list,
                            -1)

    if selection is not None:
        arduino = Arduino(this, Arduino.list()[selection], 57600)
    else:
        exit()

def draw():
    background(200)
    textAlign(CENTER)
    for i in range(14):  # from 0 to 13
        if arduino.digitalRead(i) == Arduino.HIGH:
            fill(255)
        else:
            fill(0)
        rect(420 - i * 30, 30, 20, 20)
        fill(0)
        text(str(i), 430 - i * 30, 65)

    # Draw a circle whose size corresponds to the value of an analog input.
    
    for i in range(6):  # for analog pins from A0 to A5
        noFill()
        s = arduino.analogRead(i) / 16
        ellipse(280 + i * 30, 220, s, s)
        fill(0)
        text("A" + str(i), 280 + i * 30, 180)
