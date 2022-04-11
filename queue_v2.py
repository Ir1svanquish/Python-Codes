# Queue
# Version 2

class Queue:
    """ A class representing queues of integers """

    def __init__(self, maxsize=10):
        """ Initialize the queue with an empty list and a size
        limit """
        self.qlst = []
        self.maxsize = maxsize

    def enqueue(self, item):
        """ Add an element to the back of a non-full queue """
        if self.isfull():
            print('The queue is full and no new element can be added!')
        else:
            if isinstance(item, int):
                self.qlst.append(item)
            else:
                print('You can only add integers to the queue!')

    def dequeue(self):
        """ Remove an element from the front of a non-empty queue """
        if self.isempty():
            print('The queue is empty and there is no front element!')
        else:
            print(self.qlst.pop(0))

    def isempty(self):
        """ Check whether the queue is empty """
        return len(self.qlst) == 0

    def isfull(self):
        """ Check whether the queue is full """
        return len(self.qlst) == self.maxsize

    def count(self):
        """ Return the number of elements in the queue """
        print('Number of elements in the queue =', len(self.qlst))

    def __str__(self):
        """ Print out all the elements in the queue """
        s = ""
        for i in range(len(self.qlst)):
            s += 'Element {0:d} in the queue = '.format(i+1)
            s += '{0:d}\n'.format(self.qlst[i])
        return s[:-1]
