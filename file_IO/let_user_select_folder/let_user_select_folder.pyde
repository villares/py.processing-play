from os import listdir
from os.path import isfile, join

def setup():
    selectFolder("Select a folder to process:", "folderSelected")

def folderSelected(selection):
    if selection == None:
        print("Window was closed or the user hit cancel.")
    else:
        print("User selected " + selection.getAbsolutePath())
        mypath = dataPath("").getAbsolutePath()
        for f in listdir(mypath):
            if isfile(join(mypath, f)):
                print(f)
