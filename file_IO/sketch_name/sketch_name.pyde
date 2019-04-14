def setup():
    println(sketch_name())

def sketch_name():
    """
    print the sketch name (same as the folder name - no exetension)
    """
    from os import path
    sketch = sketchPath()
    name = path.basename(sketch)
    return name
