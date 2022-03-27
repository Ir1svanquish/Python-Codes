# sphere.py
# This program defines the class Sphere for representing spheres.

import math

class Sphere:
    def __init__(self, radius):
        self.radius = radius
    def getRadius(self):
        return self.radius
    def surfaceArea(self):
        return 4 * math.pi * self.radius ** 2
    def volume(self):
        return 4 * math.pi * self.radius ** 3 / 3
