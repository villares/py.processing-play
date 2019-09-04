

def setup():
    # call-back based folder selection
    selectFolder("Select a folder to process:", "folderSelected")
    background(0)

def draw():
    ellipse(50, 50, frameCount, frameCount)

def folderSelected(selection):
    """will be executed after user interacts with selection window"""
    from os import listdir
    from os.path import isfile, join
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        path = selection.getAbsolutePath()
        print("User selected " + path)
        print("-----------------------------------------")
        for f in listdir(path):
            if isfile(join(path, f)):
                print(f)
