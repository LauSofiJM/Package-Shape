# Package-Shape
_Now I hate to read the uncolored words or the white ones._ As I wrote you, I'd like to know, if possible, what are being my mistakes. I cross my heart that I have searched many ways to fix that but it keeps giving me the same error.
***
### Better Comments
_This is the how I decided to use the extension._
- #Info related to the program (grey)
- #* Titles (green light)
- #? Advices or clarifications (blue)
- #todo Need to reforce (orange)
- #! Confused bout' something (red)
- #// Discarted (--)
- #- Success (yellow)
***
## Package
I started by creating the package named "shapes" in which I added a module named *shape.py* with the Shape class, *triangle.py* and *rectangle.py*, and of course, the *init.py*

```markdown
shapes/
├── __init__.py
├── shape.py
├── triangle.py
└── rectangle.py
```
<img width="581" alt="Package Shape" src="https://github.com/LauSofiJM/Package-Shape/assets/159340280/f42388d1-0f6f-4333-b8c9-c6ff9e81a126">

<img width="371" alt="Package Shape VS" src="https://github.com/LauSofiJM/Package-Shape/assets/159340280/4557a04b-fe16-46b2-9e3b-fc7dcd89ced2">

I split the original Shape code into the four corresponding modules this way:
I tried to follow the advice given by Santiago Rocha but I didn't understand how to implement it. That is the reason why the init is so empty.
## __init__.py
```python
from shapes.shape import Point, Line, Shape
from shapes.triangle import Triangle
from shapes.rectangle import Rectangle
```
<img width="883" alt="Shape error" src="https://github.com/LauSofiJM/Package-Shape/assets/159340280/224954cc-910f-438a-a1e7-e91c478eafa9">

___
## shape.py
```python
import math
from typing import List

#*Figures and shapes
#Practizing polimorphism and heritance

class Point:
    def __init__(self, x, y):
        self._x = x
        self._y = y

    def get_x(self):
        return self._x

    def get_y(self):
        return self._y

    @staticmethod
    def get_point():
        # Prompt the user to enter the coordinates of a point
        x = float(input("Enter the x-coordinate of the vertex: "))
        y = float(input("Enter the y-coordinate of the vertex: "))
        return Point(x, y)

class Line:
    def __init__(self, start: Point, end: Point):
        self._start = start
        self._end = end

    def get_start(self):
        return self._start

    def get_end(self):
        return self._end

    def compute_length(self):
        length = math.sqrt((self._end.get_x() - self._start.get_x())**2 + (self._end.get_y() - self._start.get_y())**2)
        return abs(length)

class Shape(Line):
    def __init__(self, is_regular: bool, vertices: List[Point], edges: List[Line], inner_angles: List[float], width: float, height: float):
        self._is_regular = is_regular
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles
        self._width = width
        self._height = height

    def get_is_regular(self):
        return self._is_regular

    def set_is_regular(self, is_regular):
        self._is_regular = is_regular

    def get_vertices(self):
        return self._vertices

    def set_vertices(self, vertices):
        self._vertices = vertices

    def get_edges(self):
        return self._edges

    def set_edges(self, edges):
        self._edges = edges

    def get_inner_angles(self):
        return self._inner_angles

    def set_inner_angles(self, inner_angles):
        self._inner_angles = inner_angles

    def get_width(self):
        return self._width

    def set_width(self, width):
        self._width = width

    def get_height(self):
        return self._height

    def set_height(self, height):
        self._height = height

    def compute_area(self):
        pass

    def compute_perimeter(self):
        pass

    def compute_inner_angles(self):
        pass
```
I just added the Point, Line and Shape classes to its own module.

___
## triangle.py

<img width="877" alt="Triangle VS" src="https://github.com/LauSofiJM/Package-Shape/assets/159340280/20f80fca-c712-4ee8-bf85-3fee47db91f9">

```python
from shapes.shape import Shape, Point, Line, math, List

class Triangle(Shape):
    def __init__(self, is_regular: bool, vertices: List[Point], edges: List[Line], inner_angles: List[float]):
        super().__init__(is_regular, vertices, edges, inner_angles, 0, 0)

        self._is_regular = input("Is the triangle regular? (y/n): ") #? If the triangle is regular, then the thiangle is equilateral.
        if self._is_regular == "y":
            self._is_regular = True

            print("\nThis is an equilateral triangle.")

            length = float(input("\nEnter the length of the first edge: "))

            print("\nEnter the coordinates of the first vertex")
            first_vertex = Point.get_point()
            second_vertex = Point(first_vertex.get_x() + length, first_vertex.get_y())
            third_vertex = Point(first_vertex.get_x() + length/2, first_vertex.get_y() + length)

            self._vertices = [first_vertex, second_vertex, third_vertex]
            self._edges = [length, length, length]
            self._inner_angles = [60, 60, 60]

        elif self._is_regular == "n":
            self._is_regular = False
            first_length = float(input("Enter the length of the first edge: "))

            print("\nEnter the coordinates of the first vertex")
            first_vertex = Point.get_point()
            second_vertex = Point(first_vertex.get_x() + first_length, first_vertex.get_y())
            print("\nEnter the coordinates of the third vertex")
            third_vertex = Point.get_point()
            vertices = [first_vertex, second_vertex, third_vertex]

            compute_length = Line.compute_length
            half = (first_vertex.get_x() + first_length) - (first_length / 2) #? This is the half of the base of the triangle.
            if third_vertex.get_x() == half:
                print ("\nThis is an isosceles triangle.")

                second_length = compute_length(Line(first_vertex, third_vertex))
                third_length = second_length

                self._vertices = [first_vertex, second_vertex, third_vertex]
                self._edges = [first_length, second_length, third_length]

                self._inner_angles = [0, 0, 0]
                self._inner_angles[0] = math.degrees(math.acos((first_length**2 - second_length**2 - third_length**2) / (-2 * second_length * third_length)))
                self._inner_angles[1] = self._inner_angles[0]
                self._inner_angles[2] = 180 - self._inner_angles[0] * 2

            elif third_vertex.get_x() != half and third_vertex.get_x() != first_vertex.get_x():
                print("\nThis is a scalene triangle.")
                second_length = compute_length(Line(first_vertex, third_vertex))
                third_length = compute_length(Line(second_vertex, third_vertex))
                self._vertices = [first_vertex, second_vertex, third_vertex]
                self._edges = [first_length, second_length, third_length]

                self._inner_angles = [0, 0, 0]
                self._inner_angles[0] = math.degrees(math.acos((first_length**2 - second_length**2 - third_length**2) / (-2 * second_length * third_length)))
                self._inner_angles[1] = math.degrees(math.acos((second_length**2 - first_length**2 - third_length**2) / (-2 * first_length * third_length)))
                self._inner_angles[2] = math.degrees(math.acos((third_length**2 - first_length**2 - second_length**2) / (-2 * first_length * second_length)))
            else:
                third_vertex.get_x() != half and third_vertex.get_x() == first_vertex.get_x()
                print("\nThis is a right triangle.")
                second_length = compute_length(Line(first_vertex, third_vertex))
                third_length = math.sqrt(first_length**2 + second_length**2)
                self._vertices = [first_vertex, second_vertex, third_vertex]
                self._edges = [first_length, second_length, third_length]

                self._inner_angles = [0, 0, 0]
                self._inner_angles[0] = 90
                self._inner_angles[1] = math.degrees(math.atan(first_length / third_length))
                self._inner_angles[2] = math.degrees(math.atan(second_length / third_length))

    def compute_perimeter(self):
        return sum(self._edges)

    def compute_area(self): #? This is the Heron's formula.
        s = self.compute_perimeter() / 2
        return math.sqrt(s * (s - self._edges[0]) * (s - self._edges[1]) * (s - self._edges[2]))

    def __str__(self):
        vertices_str = ", ".join([f"({v.get_x()}, {v.get_y()})" for v in self._vertices])
        edges_str = ", ".join([f"{ed}" for ed in self._edges])
        angles_str = ", ".join([f"{angles}" for angles in self._inner_angles])
        permiter = self.compute_perimeter()
        area = self.compute_area()
        return f"\nTriangle: \nVertices: {vertices_str}\n\nEdges: {edges_str}\n\nInner Angles: {angles_str}\n\nPerimeter: {permiter}\n\nArea: {area}"

triangle = Triangle(True, [], [], [])
print(triangle)
```
I added the triangle class to its module and tried to import Shape, Point, Line, math and List from shapes.

## rectangle.py
<img width="811" alt="Rectangle VS" src="https://github.com/LauSofiJM/Package-Shape/assets/159340280/63e738d6-c88f-4bfc-a03a-e0ef4d6aa7e3">

```python
from shapes.shape import Shape, Point, Line, List

class Rectangle(Shape):
    def __init__(self, is_regular: bool, vertices: List[Point], edges: List[Line], inner_angles: List[float], width: float, height: float):
        super().__init__(is_regular, vertices, edges, inner_angles, width, height)
        self._width = width
        self._height = height
        self._vertices = vertices
        self._edges = edges
        self._inner_angles = inner_angles

        self._is_regular = input("\nIs the rectangle regular? (y/n): ") #? If the rectangle is regular, then the rectangle is a square.
        if self._is_regular == "y":
            self._is_regular = True

            print("\nThis is a square.")
            length = float(input("Enter the length of one side: "))
            print("Enter the coordinates of the first vertex")
            first_vertex = Point.get_point()

            second_vertex = Point(first_vertex.get_x() + length, first_vertex.get_y())
            third_vertex = Point(first_vertex.get_x(), first_vertex.get_y() + length)
            fourth_vertex = Point(first_vertex.get_x() + length, first_vertex.get_y() + length)

            self._vertices = [first_vertex, second_vertex, third_vertex, fourth_vertex]
            self._edges = [length, length, length, length]
            self._inner_angles = [90, 90, 90, 90]
            self._width = length
            self._height = length

        elif self._is_regular == "n":
            self._is_regular = False

            width = float(input("\nEnter the width of the rectangle: "))
            height = float(input("Enter the height of the rectangle: "))

            print("\nEnter the coordinates of the first vertex: ")
            first_vertex = Point.get_point()
            second_vertex = Point(first_vertex.get_x() + width, first_vertex.get_y())
            third_vertex = Point(first_vertex.get_x(), first_vertex.get_y() + height)
            fourth_vertex = Point(first_vertex.get_x() + width, first_vertex.get_y() + height)

            self._vertices = [first_vertex, second_vertex, third_vertex, fourth_vertex]
            self._edges = [width, width, height, height]
            self._inner_angles = [90, 90, 90, 90]
            self._width = width
            self._height = height

    def compute_perimeter(self):
        return sum(self._edges)

    def compute_area(self):
        return self._width * self._height

    def __str__(self):
        vertices_str = ", ".join([f"({v.get_x()}, {v.get_y()})" for v in self._vertices])
        edges_str = ", ".join([f"{ed}" for ed in self._edges])
        angles_str = ", ".join([f"{angles}" for angles in self._inner_angles])
        perimeter = self.compute_perimeter()
        area = self.compute_area()
        return f"Rectangle: \nVertices: {vertices_str}\n\nEdges: {edges_str}\n\nInner Angles: {angles_str}\n\nPerimeter: {perimeter}\n\nArea: {area}"

rectangle = Rectangle(True, [], [], [], 0, 0)
print(rectangle)
```
I added the rectangle class to its module and tried to import Shape, Point, Line and List from shapes.
The images I added allow me to show you that there are no visible syntax errors or related issues in the code.
