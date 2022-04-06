# Exercise 3
# Queue
# Name: Chan kit Chi UID: 3035779167 Written on: 06/04

class Queue:
    
    def __init__(self, maxsize = 10):
        self.qlst = []
        self.maxsize = maxsize

    def enqueue(self, item):
        if isinstance(item, int):
            if len(self.qlst) < self.maxsize:
                self.qlst.append(item)
            else:
                print("The queue is full and no new element can be added!")
        else:
            print("You can only add integers to the queue!")

    def dequeue(self):
        if len(self.qlst) > 0:
            result = self.qlst.pop(0)
            print(result)
        else:
            print("The queue is empty and there is no front element!")

    def isempty(self):
        if len(self.qlst) == 0:
            print ("True")
        else:
            print("False")

    def isfull(self):
        if len(self.qlst) == self.maxsize:
            print ("True")
        else:
            print("False")

    def count(self):
        print("Number of elements in the queue = ", len(self.qlst))

    def __str__(self):
        result = ""
        for i in range(len(self.qlst) - 1):
            result += f"Element {i + 1} in the queue = {self.qlst[i]}\n"
        result += f"Element {len(self.qlst)} in the queue = {self.qlst[len(self.qlst) -1 ]}"
        return result
