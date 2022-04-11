# quadratic.py
# Quadrilaterals, Trapezoids, Parallelograms, and Squares

# Import the Point class and the isclose function from the math module
from math import isclose
from point import Point

class Quadrilateral:
    """ A class representing quadrilaterals """

    def __init__(self, x1, y1, x2, y2, x3, y3, x4, y4):
        """ Initialize the quadrilateral with its four endpoints """
        self.pt1 = Point(x1, y1)
        self.pt2 = Point(x2, y2)
        self.pt3 = Point(x3, y3)
        self.pt4 = Point(x4, y4)

    def getpt1(self):
        """ Return the first endpoint of the quadrilateral """
        return self.pt1

    def getpt2(self):
        """ Return the second endpoint of the quadrilateral """
        return self.pt2

    def getpt3(self):
        """ Return the third endpoint of the quadrilateral """
        return self.pt3

    def getpt4(self):
        """ Return the fourth endpoint of the quadrilateral """
        return self.pt4

    def getcoorstr(self):
        """ Return a string containing the coordinates of the endpoints
        of the quadrilateral """
        return '{0}, {1}, {2}, {3}'.format(self.pt1, self.pt2,
                                           self.pt3, self.pt4)

    def __str__(self):
       """ Return a string representation of the quadrilateral """
       return 'Coordinates of the Quadrilateral are:\n' + self.getcoorstr()

class Trapezoid(Quadrilateral):
    """ A class representing trapezoids """

    def getheight(self):
        """ Return the height of the trapezoid """
        if isclose(self.getpt1().gety(), self.getpt2().gety()):
            return abs(self.getpt2().gety() - self.getpt3().gety())
        else:
            return abs(self.getpt1().gety() - self.getpt2().gety())

    def getsumoftwosides(self):
        """ Return the sum of the two parallel sides of the trapezoid """
        if isclose(self.getpt1().gety(), self.getpt2().gety()):
            return abs(self.getpt1().getx() - self.getpt2().getx()) +\
                   abs(self.getpt3().getx() - self.getpt4().getx())
        elif isclose(self.getpt1().gety(), self.getpt3().gety()):
            return abs(self.getpt1().getx() - self.getpt3().getx()) +\
                   abs(self.getpt2().getx() - self.getpt4().getx())
        else:
            return abs(self.getpt1().getx() - self.getpt4().getx()) +\
                   abs(self.getpt2().getx() - self.getpt3().getx())

    def getarea(self):
        """ Return the area of the trapezoid """
        return 0.5*self.getsumoftwosides()*self.getheight()

    def __str__(self):
        """ Return a string representation of the trapezoid """
        return 'Coordinates of the Trapezoid are:\n'\
                +self.getcoorstr()+'\n'\
                +'Height is: {:.1f}\n'.format(self.getheight())\
                +'Area is: {:.2f}'.format(self.getarea())

class Parallelogram(Trapezoid):
    """ A class representing parallelograms """

    def getwidth(self):
        """ Return the width of the parallelogram """
        if isclose(self.getpt1().gety(), self.getpt2().gety()):
            return abs(self.getpt1().getx() - self.getpt2().getx())
        elif isclose(self.getpt1().gety(), self.getpt3().gety()):
            return abs(self.getpt1().getx() - self.getpt3().getx())
        else:
            return abs(self.getpt1().getx() - self.getpt4().getx())

    def __str__(self):
        """ Return a string representation of the parallelogram """
        return 'Coordinates of the Trapezoid are:\n'\
                +self.getcoorstr()+'\n'\
                +'Width is: {:.1f}\n'.format(self.getwidth())\
                +'Height is: {:.1f}\n'.format(self.getheight())\
                +'Area is: {:.2f}'.format(self.getarea())

class Square(Parallelogram):
    """ A class representing squares """
    def __str__(self):
        """ Return a string representation of the square """
        return 'Coordinates of the Square are:\n'\
        +self.getcoorstr()+'\n'\
        +'Side is: {:.1f}\n'.format(self.getwidth())\
        +'Area is: {:.2f}'.format(self.getarea())
