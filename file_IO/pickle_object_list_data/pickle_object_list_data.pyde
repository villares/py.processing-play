"""
Based on Loading Tabular Data example by Daniel Shiffman.  
"""
from Bubble import Bubble
from input_message import input
import pickle


bubbles = []

def setup():
    size(640, 360)
    loadData()

def draw():
    background(255)
    # Display all bubbles
    for b in bubbles:
        b.display()
        b.rollover(mouseX, mouseY)

    textAlign(LEFT)
    fill(0)
    text("Click to add bubbles.", 10, height - 10)


def loadData():
    # Load CSV file into a Table object
    global bubbles
    with open("data/bubbles.data", "rb") as f2:
        bubbles = pickle.load(f2)

def mousePressed():
    name = input("Name:")
    bubbles.append(Bubble(mouseX,
                          mouseY,
                          random(40, 80),
                          name)) 
    # If the list has more than 10 objects
    if len(bubbles) > 10:
        # Delete the oldest Buuble
        bubbles.pop(0)
    # WARNING: on Save you have to put the folder :(
    with open("data/bubbles.data", "wb") as file:
        pickle.dump(bubbles, file)

    loadData()
