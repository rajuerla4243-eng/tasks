class Shape:
    def area(self):
        print("Calculate area")

class Rectangle(Shape):
    def rectangle_area(self):
        print("Area of rectangle")

class Circle(Shape):
    def circle_area(self):
        print("Area of circle")

r = Rectangle()
c = Circle()

r.area()
r.rectangle_area()

c.area()
c.circle_area()