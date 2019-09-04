"""
Based on Loading Tabular Data example by Daniel Shiffman.  
"""
from Bubble import Bubble
from input_message import input

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
    global table
    global bubbles
    # "header" option indicates the file has a header row
    table = loadTable("data.csv", "header")
    bubbles = []

    for row in table.rows():
        # You can access the fields via their column name (or index)
        x = row.getFloat("x")
        y = row.getFloat("y")
        d = row.getFloat("diameter")
        n = row.getString("name")
        # Make a Bubble object out of the data read
        bubbles.append(Bubble(x, y, d, n))


def mousePressed():
    global table
    # Create a new row
    row = table.addRow()
    # Set the values of that row
    row.setFloat("x", mouseX)
    row.setFloat("y", mouseY)
    row.setFloat("diameter", random(40, 80))
    name = input("Name:")
    row.setString("name", name)

    # If the table has more than 10 rows
    if table.getRowCount() > 10:
        # Delete the oldest row
        table.removeRow(0)

    # WARNING: on Save you have to put the folder :(
    saveTable(table, "data/data.csv")
    # Reload
    loadData()
