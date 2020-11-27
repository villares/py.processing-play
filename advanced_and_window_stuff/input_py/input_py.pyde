def setup():
    answer = input('enter your name')
    if answer:
        println('hi ' + answer)
    elif answer == "":
        println("[empty]")
    else:
        println(answer) # Canceled dialog will print None

def input(question='', suggestion=''):
    from javax.swing import JOptionPane
    return JOptionPane.showInputDialog(None, question, suggestion)
