from abc import ABC, abstractmethod
import math


class Shape(ABC):
    @abstractmethod
    def area(self):
        pass


class Circle(Shape):
    def area(self, r):
        print("area of  a circle:",math.pi* r * r)


class Cone(Shape):
    def area(self, r, l):
        print("area of a cone:", math.pi* r * (r + l))


obj1 = Circle()
obj1.area(4)
obj2 = Cone()
obj2.area(2, 4)
