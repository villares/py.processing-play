from os import listdir
from os.path import isfile, join

data_path = sketchPath("data")
for f in listdir(data_path):
    if isfile(join(data_path, f)):
        print(f)
