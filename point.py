# point.py
# Written by F K Chow, HKU
# Last update: 2022/2/21

class Point:
    """ A class representing geometric points """
    
    def __init__(self, x, y):
        """ Initialize the point with its x, y coordinates """
        self.x = x
        self.y = y

    def getx(self):
        """ Return the x coordinate of the point """
        return self.x

    def gety(self):
        """ Return the y coordinate of the point """
        return self.y

    def __str__(self):
        """ Return a string representation of the point """
        return '({:.1f}, {:.1f})'.format(self.x, self.y)
