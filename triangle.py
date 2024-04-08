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