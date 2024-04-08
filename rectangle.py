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