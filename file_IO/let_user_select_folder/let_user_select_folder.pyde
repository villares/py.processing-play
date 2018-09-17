from os import listdir
from os.path import isfile, join

def setup():
    selectFolder("Select a folder to process:", "folderSelected")

def folderSelected(selection):
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        path = selection.getAbsolutePath()
        print("User selected " + path)
        print("-----------------------------------------")
        for f in listdir(path):
            if isfile(join(path, f)):
                print(f)
