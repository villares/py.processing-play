from __future__ import unicode_literals

def setup():
    size(400, 300, P2D)
    println(option_pane("Escolha uma opção",
                        "qual destes?",
                        ["A", "B", "C"],
                        "B")
            )

def option_pane(title, message, options, default=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(
        frame,
        message,
        title,
        JOptionPane.INFORMATION_MESSAGE,
        None,  # return on cancel
        options,
        default)  # must be in options, otherwise 1st is shown

def draw():
    pass
