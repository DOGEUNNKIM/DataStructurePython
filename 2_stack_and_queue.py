# stack
# limited access
# LIFO(last in first out)
# push, pop

from ctypes import sizeof


class Stack: 
    def __init__(self):
        self.item =[]

    def push(self, val):
        self.item.append(val)

    def pop(self):
        try:
            return self.item.pop()
        except IndexError:
            print("Empty!")

    def top(self):
        try:
            return self.item[-1]
        except IndexError:
            print("Empty!")

    def len(self):
        return len(self.item)
        
ex1 = Stack()

ex1.push(10)
ex1.push(20)
ex1.push(30)
ex1.push(40)
print(len(ex1.item))

print(ex1.pop())
print(ex1.pop())
print(ex1.pop())
print(ex1.pop())
print(ex1.pop())
print(len(ex1.item))

# queue
# FIFO(first in first out)
# enqueue, dequeue
class Queue:
    def __init__(self):
        self.item=[]

    def enqueue(self,val):
        self.item.append(val)

    def dequeue(self):
        try:
            temp = self.item[0]
            self.item.remove(temp)
            return temp
        except IndexError:
            print("Empty!")

    def len(self):
        return len(self.item)

ex1 = Queue()

ex1.enqueue(10)
ex1.enqueue(20)
ex1.enqueue(30)
ex1.enqueue(40)
print(len(ex1.item))

print(ex1.dequeue())
print(ex1.dequeue())
print(ex1.dequeue())
print(ex1.dequeue())
print(ex1.dequeue())
print(len(ex1.item))


