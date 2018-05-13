from __future__ import unicode_literals

add_library('serial')  # import processing.serial.*;
add_library('arduino')  # import cc.arduino.*;

lista_portas = [str(num) + ": " + porta_serial for num, porta_serial
                in enumerate(Arduino.list())]

def setup():
    size(400, 300, P2D)
    println(option_pane("Sua lousa está conectada?",
                        "indique em qual porta:",
                        lista_portas,
                        -1)
            )

def option_pane(title, message, options, default=None, index_only=True):
    from javax.swing import JOptionPane
    
    if default == None:
        default = options[0]
    elif index_only:
        default = options[default]
        
    selection = JOptionPane.showInputDialog(
        frame,
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,  # for Java null
        options,
        default)  # must be in options, otherwise 1st is shown
    if selection:
        if index_only:
            return options.index(selection)
        else:
            return selection

def draw():
    pass
