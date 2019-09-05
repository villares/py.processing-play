
urls = ["https://processing.org/img/processing-web.png", 
        "https://processing.org/reference/images/loadImage_0.png", 
        ]
        
results = []

def setup():
    size(500, 500)
    thread("load_remote_images")
    
def draw():
    print(len(results))
    
    
def load_remote_images():
    for url in urls:
        img = loadImage(url)
        if img:
            results.append(img)
    print("loaded")
    
    
