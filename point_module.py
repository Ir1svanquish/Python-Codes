# point_module.py
# This program defines the base class Point for representing geometric
# points, the derived class Circle for representing circles, and the
# derived Cylinder for representing cylinders.

import math

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y
        
    def __str__(self):
        return "({:d}, {:d})".format(self.x, self.y)
    
class Circle(Point):
    def __init__(self, x = 0, y = 0, radius = 0.0):
        Point.__init__(self, x, y)
        self.radius = radius
        
    def area(self):
        return math.pi * self.radius ** 2
    
    def __str__(self):
        return "Center = {:s}, Radius = {:f}".format(Point.__str__(self), self.radius)

class Cylinder(Circle):
    def init (self, x = 0, y = 0, radius = 0.0, height = 0.0):
        Circle.__init__(self, x, y, radius)
        self.height = height
        
    def area(self):
        return 2 * Circle.area(self) + 2 * math.pi * self.height * self.radius
    
    def volume(self):
        return Circle.area(self) * self.height
    
    def __str__(self):
        return "{:s}, Height = {:f}".format(Circle.__str__(self), self.height)
