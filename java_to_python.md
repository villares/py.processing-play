

# Tips for porting Processing code from Java mode to Python mode

>… And possibly vice versa :)

### Getting started

- Comments with `//` in Java become comments with `#`. Multiline comments with `/ *… * /` can be converted to *docstrings*, with triple quotes in Python, `""" ... """`.

- Java is a *static typing* language and Python is a *dynamic typing* language which means that we will remove all type declarations. Remove `int`, `float`,` String`, `color`,` boolean` from variable declarations. For example, `int i = 0; `becomes ` i = 0`.

- We should also remove `void` or any type declaration from a function definition, replacing it with Python's ` def`. Also remove the type declaration from the function parameters.

   **Java**
  
  ```java
  float media (float a, float b) {
    return (a + b) / 2;
  }
  ```
  **Python**
  
  ```python
  def media (a, b):
      return (a + b) / 2
  ```
- It is common for the indentation of the Java code to reflect the hierarchy of instruction blocks, even if this is not mandatory (in Java the braces`{}` rule), use the IDE auto-formatting tool before you start!
- The braces need to be removed, and you should replace each `{` with `:` at the beginning of an instruction block (this is not true for *array definitions*, which have braces but are not an instruction block, and will probably become a list or tuple with `[]` or` () `.
- Remove the `;` at the end of the lines.

### A table with equivalences for conversion

Boolean values ​​in Java are `true` and` false`, in Python they are `True` and` False`. Let's make a chart with the logical operators and some other equivalences.

| Java | Python |
| ------------------------------------------------ | ------------------------------------------ |
| `void func () {…}` | `def func ():…` |
| `true` and` false` | True and False |
| ``` a && b``` (** and ** logical) | `a and b` |
| `a || b` (** or ** logical) | `a or b` |
| `! a` (** no ** logical) | `not a` |
| `i ++` (increment) | `i + = 1` |
| `i -` (decrement) | `i - = 1` |
| `a <= b && b <c` | `a <= b <c` |
| `for (int i = 0; i <limit; i ++) {…` | `for i in range (limit):…` |
| `for (int i = start; i <limit; i += step) {…` | `for i in range (start, limit, step):…` |
| `for (Ball b: arrayListOfBalls) {…` | `for b in listOfBalls:…` |

Similar to `null` in Java we have the value ` None` in Python they are not totally equivalent but it is a good guess to make the substitution.

### Looping with `for`

The simplest case is a `for` based on any counter, such as ` for (int i = 0; i <limit; i++) {… ` which translates to `for i in range (limit): ... ` and the so-called *for each* loop, shown in the box, is also very straightforward.

As the `range()`based for construct in Python works only with integers, so if you have a Java `for` loop with a *float* step, you'll have to convert it to a `while` loop.

**Java**

```java
float angleStep = TWO_PI / 18
for (float angle=0; angle < TWO_PI; angle += angleStep){ 
    …
}
```

**Pyton**

```python
angleStep = TWO_PI / 18
angle = 0
while angle < TWO_PI:
    …
    angle += angleStep
```

Here an example of a loop made just to get objects from a data structure:


```java
for (int i = 0; i <my_array.length; i ++) {
  something(my_array [i]);
}
```

**Python**

```python
for item in my_list:
    something(item)
```
or, if you need the index.
```python
for i, item in enumerate (my_list):
    something(i, item)
```

Here is a reversed iteration for removing items from an *ArrayList* in Java, a list in Python:

**Java**

```java
for (int i = particles.size () - 1; i> = 0; i--) {
  Particle p = particles.get (i);
  p.run ();
  if (p.isDead ()) {
    particles.remove (i);
  }
}
```

**Python**

```python
for p in reversed (particles):
    p.run ()
    if p.isDead ():
        del p
```

or, if you need the index:

```python
for i in reversed (range (len (particles))):
    p = particles [i]
    p.run ()
    if p.isDead ():
        del particles [i]
```

or yet:

```python
for i, p in reversed (list (enumerate (self.particles))):
    p.run ()
    if p.isDead ():
        del p # or del self.particles [i]
```

### `if`,` else` and their friends

Note that the `if` condition in Python does not have the required parentheses in Java. The combination of an `else if` turns into an` elif` contraction.

**Java**

```java
for (int i = 2; i <width-2; i + = 2) {
  if ((i% 20) == 0) {
    stroke (255);
    line (i, 80, i, height / 2);
  } else if ((i% 10) == 0) {
    stroke (153);
    line (i, 20, i, 180);
  } else {
    stroke (102);
    line (i, height / 2, i, height-20);
  }
}
```
**Python**

```python
for i in range(2, width - 2, 2):
    # If 'i' divides by 20 with no remainder
    if i % 20 == 0:
        stroke(255)
        line(i, 80, i, height / 2)
    elif i % 10 == 0:
        stroke(153)
        line(i, 20, i, 180)
    else:
        stroke(102)
        line(i, height / 2, i, height - 20)
```

#### Ternary operator

**Java**

```java
result = cond? a: b
```

**Python**

```python
result = a if cond else b
```

#### switch & case

There is no `switch / case` in Python, you can change it to a sequence of `if / elif` or, if just to call different functions, a function dictionary [TO DO page about it].

### Global variables

If the variable is *declared and initialized* (type and value are defined) at the beginning of the sketch just remove the type declaration, but since there is no Python declaration of a variable without making an assignment, when the variable is only declared (a type is indicated without *initialization*) at the beginning of the sketch we need to see where it is calculated the first time and add, at the beginning of the function, the statement `global variable_name`.

In fact, every function that changes the assignment of global variables in its body needs the `global` statement with the names of the variables that are modified.

An example:

**Java**

```java
int rad = 60; // Width of the shape
float xpos, ypos; // Starting position of shape
float xspeed = 2.8; // Speed of the shape
yspeed float = 2.2; // Speed of the shape
int xdirection = 1; // Left or Right
int ydirection = 1; // Top to Bottom

void setup ()
{
  size (600, 300);
  // Set the starting position of the shape
  xpos = width / 2;
  ypos = height / 2;
}

void draw ()
{
  background (102);
  xpos = xpos + (xspeed * xdirection);
  ypos = ypos + (yspeed * ydirection);
    
  if (xpos> width-rad || xpos <rad) {
    xdirection * = -1;
  }
  if (ypos> height-rad || ypos <rad) {
    ydirection * = -1;
  }

  ellipse (xpos, ypos, rad * 2, rad * 2);
}
```

**Python**

```python
rad = 60; # Width of the shape
# In the original it had: float xpos, ypos; // Starting position of shape
xspeed = 2.8; # Speed of the shape
yspeed = 2.2; # Speed of the shape
xdirection = 1; # Left or Right
ydirection = 1; # Top to Bottom

def setup (): **Python**
    size (600, 300)
    global xpos, ypos # xpos, ypos are global created in the setup
    noStroke ()
    xpos = width / 2
    ypos = height / 2

def draw ():
    global xpos, ypos, xdirection, ydirection # will be changed!
    background (102)
    xpos + = xspeed * xdirection
    ypos + = yspeed * ydirection
    
    if xpos <rad or width - rad <xpos: # note that rad is not changed
        xdirection * = -1
    if ypos <rad or height - rad <ypos:
        ydirection * = -1
    ellipse (xpos, ypos, rad * 2, rad * 2)
```

### Importing libraries and other sketch tabs

In Java mode Processing the libraries are imported with `import` but in Python mode this instruction is more used to import * modules * from the standard Python library, and **. Py ** files like the other IDE tabs, which unlike Java mode are not automatically part of sketch.

Use the menu command ** Sketch> Import Library .. ** (or * Sketch> Import Library ... * in English) to add the line with `add_library ()` with the correct argument.

**Java**

```java
import com.hamoid. *; // VideoExport library
```

**Python**

```python
add_library ('VideoExport') # the same Video Export library
```

### Object orientation

#### Getting an instance and accessing methods and attributes

Java needs the keyword **`new`** to create an instance of a class, just remove it! Access to methods and attributes is exactly the same.

**Java**

```java
VideoExport videoExport;

void setup () {
  size (600, 600);
  videoExport = new VideoExport (this);
  videoExport.startMovie ();
}
```

**Python**

``` python
def setup ():
    global videoExport
    size (600, 600)
    videoExport = VideoExport (this)
    videoExport.startMovie ()
```

#### Declaring a class

Class declarations change slightly, roughly, the `__init __ (self)` method plays the role of the *constructor* method of a Java class. See the `MRect` class in the example **Basics > Objects > Objects** that comes with the Processing IDE. You'll have to add `self` as the first parameter of each method, and `self.` to access it's members, methods & attributes.

**Java**

```java
class MRect 
{
  int w; // single bar width
  float xpos; // rect xposition
  float h; // rect height
  float ypos ; // rect yposition
  float d; // single bar distance
  float t; // number of bars
 
  MRect(int iw, float ixp, float ih, float iyp, float id, float it) {
    w = iw;
    xpos = ixp;
    h = ih;
    ypos = iyp;
    d = id;
    t = it;
  }
 
  void move (float posX, float posY, float damping) {
    float dif = ypos - posY;
    if (abs(dif) > 1) {
      ypos -= dif/damping;
    }
    dif = xpos - posX;
    if (abs(dif) > 1) {
      xpos -= dif/damping;
    }
  }
 
  void display() {
    for (int i=0; i<t; i++) {
      rect(xpos+(i*(d+w)), ypos, w, height*h);
    }
  }
}
```

**Python**

```python
class MRect:

    def __init__(self, iw, ixp, ih, iyp, id, it):
        self.w = iw  # single bar width
        self.xpos = ixp  # rect xposition
        self.h = ih  # rect height
        self.ypos = iyp  # rect yposition
        self.d = id  # single bar distance
        self.t = it  # number of bars

    def move(self, posX, posY, damping):
        self.dif = self.ypos - posY
        if abs(self.dif) > 1:
            self.ypos -= self.dif / damping

        self.dif = self.xpos - posX
        if abs(self.dif) > 1:
            self.xpos -= self.dif / damping

    def display(self):
        for i in range(self.t):
            rect(self.xpos + (i * (self.d + self.w)),
                 self.ypos, self.w, height * self.h)
```