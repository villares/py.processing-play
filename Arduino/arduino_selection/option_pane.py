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
