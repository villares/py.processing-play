from __future__ import unicode_literals
from option_pane import option_pane

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

port_list = [str(num) + ": " + porta_serial for num, porta_serial
                in enumerate(Arduino.list())]

def setup():
    size(400, 300, P2D)
    selection = option_pane("Is your Arduino board connected?",
                        "Select the USB port:",
                        port_list,
                        -1)
            
    if selection is not None:
        arduino = Arduino(this,  Arduino.list()[selection], 57600)
    else:
        exit()
        

def draw():
    pass
