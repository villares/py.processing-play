def setup():
    file_names = list_files("out")
    
    for fn in file_names:
        println(fn)

def list_files(dir="data"):
    from os import listdir
    from os.path import isfile, join
    data_path = sketchPath(dir)
    try:
        f_list = [f for f in listdir(data_path)
                    if isfile(join(data_path, f))]
    except OSError:
        return []
    
    return f_list
