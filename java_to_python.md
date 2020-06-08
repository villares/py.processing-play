## Tips for porting Processing Java code to Python mode

>… And possibly vice versa :)

[versão em português](https://abav.lugaralgum.com/material-aulas/Processing-Python/java_para_python)

### Getting started

- As you probably know already, Python uses indentation to place code lines 'inside' a function definition and in many other code nesting structures. In Java the braces`{}` rule, but it is common for the indentation to also reflect the code hierachy, even if this is not mandatory, so use the IDE auto-formatting tool before you start, and take care!

- The braces need to be removed, and you should replace each `{` with `:` at the beginning of an instruction block (this is not true for *array definitions*, which have braces but are not an instruction block, and will probably become a list or tuple with `[]` or `()`.

- Remove the `;` at the end of the lines.

- Comments with `//` in Java become comments with `#`. Multiline comments with `/*…*/` can be converted to *docstrings*, with triple quotes in Python, `""" … """`.

- Java is a *static typing  language* and Python is a *dynamic typing language* that means we will remove all type declarations. Remove `int`, `float`,` String`, `color`,` boolean` from variable declarations. For example, `int i = 0;` becomes `i = 0`.

- We should also remove `void` or any type declaration from a function definition, replacing it with Python's `def`. Also remove the type declaration from the function parameters.

   **Java**
  
  ```java
  float average(float a, float b) {
    return (a + b) / 2;
  }
  ```
  **Python**
  
  ```python
  def average(a, b):
      return (a + b) / 2
  ```


### A table with some equivalences for conversion

Boolean values in Java are named `true` and` false`, in Python they are `True` and` False`. Let's make a chart with the logical operators and some other equivalences.

| Java | Python |
| ------------------------------------------------ | ------------------------------------------ |
| `void func() {…}` | `def func():…` |
| `true` and` false` | `True` and `False` |
| `a && b` (logical **and**) | `a` **`and`** `b` |
| ```a || b``` (logical **or**) | `a` **`or`** `b` |
| `!a` (logical **not**) | **`not`** `a` |
| `i++` (increment) | `i += 1` |
| `i--` (decrement) | `i -= 1` |
| `a <= b && b < c` | `a <= b < c` |
| `for (int i=0; i<limit; i++) { …` | `for i in range (limit): …` |
| `for (int i=start; i<limit; i+=step) { …` | `for i in range (start, limit, step): …` |
| `for (Ball b : arrayListOfBalls) { …` | `for b in listOfBalls: …` |

Similar to `null` in Java we have the special value `None` in Python, they are not totally equivalent but it is usually a good guess to make the substitution.

### Looping with `for`

The simplest case is a `for` based on a counter, such as `for (int i=0; i<limit; i++) { …` which translates into `for i in range(limit): …` and the so-called *for each* loop, shown in the chart, is also very straightforward.

But if you have a Java `for` loop with a *float* step, as the `range()` based `for` construct in Python works only with integers, you'll have to convert it to a `while` loop like in the example below.

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
for (int i = 0; i < my_array.length; i ++) {
  something(my_array[i]);
}
```

**Python**

```python
for item in my_list:
    something(item)
```
or, if you need the index.
```python
for i, item in enumerate(my_list):
    something(i, item)
```

Here a reversed iteration for removing items from an *ArrayList* in Java, a list in Python:

**Java**

```java
for (int i = particles.size() - 1; i >= 0; i--) {
  Particle p = particles.get(i);
  p.run();
  if (p.isDead()) {
    particles.remove(i);
  }
}
```

**Python**

```python
for p in reversed(particles):
    p.run()
    if p.isDead():
        del p
```

or, if you need the index:

```python
for i in reversed(range(len(particles))):
    p = particles[i]
    p.run()
    if p.isDead():
        del particles[i]
```

or yet:

```python
for i, p in reversed(list(enumerate(self.particles))):
    p.run()
    if p.isDead():
        del p # or del self.particles[i]
```

### `if`, `else` and their friends

Note that the `if` condition in Python does not have the required parentheses as in Java. The combination of `else if`  becomes the `elif` contraction.

**Java**
```java
for (int i = 2; i < width-2; i += 2) {
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
result = cond ? a : b
```

**Python**

```python
result = a if cond else b
```

#### switch & case

There is no `switch / case` in Python, you can change it to a sequence of `if / elif` or, if just to call different functions, a function dictionary [TO DO example for this].

### Global variables

If a variable is *declared and initialized* (type and value are defined) at the beginning of the sketch just remove the type declaration.

Since there is no way in Python to declare a variable without making an assignment, when the variable is just declared (a type is set without *initialization*) at the beginning of the sketch, we need to find where it is assigned for the first time and add the `global variable_name` statementat at the beginning of that function.

In fact, every function that changes the assignment of global variables in its body needs the `global` statement with the names of the variables that are modified.

An example:

**Java**
```java
int rad = 60;       // Width of the shape
float xpos, ypos;   // Starting position of shape
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
# The original had this here: float xpos, ypos; // Starting position of shape
xspeed = 2.8;   # Speed of the shape
yspeed = 2.2;   # Speed of the shape
xdirection = 1; # Left or Right
ydirection = 1; # Top to Bottom

def setup (): **Python**
    size (600, 300)
    global xpos, ypos # xpos, ypos are assigned first here in setup
    noStroke ()
    xpos = width / 2
    ypos = height / 2

def draw ():
    global xpos, ypos, xdirection, ydirection # will be changed!
    background (102)
    xpos + = xspeed * xdirection
    ypos + = yspeed * ydirection
    
    if xpos < rad or width - rad < xpos: # note that rad is never changed
        xdirection * = -1
    if ypos < rad or height - rad < ypos:
        ydirection * = -1
    ellipse (xpos, ypos, rad * 2, rad * 2)
```

### Importing libraries and other sketch tabs

In Java mode Processing the libraries are imported with `import` but in Python mode this instruction is more often used to import *modules* from the Python's standard library, and **.py** files presented as other IDE tabs (which, unlike in Java mode, are not automatically a part of the sketch).

Use the menu command **Sketch > Import Library...** to add the line with `add_library()` with the correct argument.

**Java**

```java
import com.hamoid. *; // VideoExport library
```

**Python**

```python
add_library ('VideoExport') # the same Video Export library
```

### Object orientation

#### Getting an instance and access to its methods and attributes

Java needs the keyword **`new`** to create an instance of a class, just remove it! Access to methods and attributes is exactly the same.

**Java**

```java
VideoExport videoExport;

void setup() {
  size(600, 600);
  videoExport = new VideoExport(this);
  videoExport.startMovie();
}
```

**Python**

``` python
def setup():
    global videoExport
    size(600, 600)
    videoExport = VideoExport(this)
    videoExport.startMovie()
```

#### Declaring a class

Class declarations change slightly, roughly, the `def __init__(self …): …` method plays the role of the *constructor* method of a Java class. See the `MRect` class in the example **Basics > Objects > Objects** that comes with the Processing IDE. You'll have to add `self` as the first parameter of each method, and `self.` to access it's members, methods & attributes.

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

### Data structures

Arrays like `int[]`, `float[]` or `PVector[]` usually become lists in Python (sometimes tuples if they are created and left alone).  ArrayList is very much like a list:

**Java**

```java
ArrayList<Flag> flags; // a list of Flag de objetos

void setup() {
  size(400, 400); 
  flags = new ArrayList<Flag>();
  for (int i=0; i <50; i++) {
    flags.add(new Flag(100, 100, 12));
  }
}
```
**Python**

```python
flags = []  # a list of Flag de objetos

def setup():
    size(400, 400); 
    for i in range(50):
        flags.append(Flag(100, 100, 12))
```

#### 2D Arrays

```java
int[][] board;
board = new int[grid_w][grid_h]
```
A list of lists.

```Python
board = [[0] * grid_w for _ in range(grid_h)]
```



