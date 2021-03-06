#Jonathan Shan
#Section 15
#CPE 202

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Python List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.items = [None]*capacity
        self.num_items = 0 

    def is_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.num_items == 0:
            return True
        return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if self.num_items == self.capacity:
            return True
        return False

    def push(self, item):
        """If stack is not full, pushes item on stack. 
           If stack is full when push is attempted, raises IndexError"""
        if self.is_full():
            raise IndexError
        self.items[self.num_items] = item
        self.num_items += 1

    def pop(self): 
        """If stack is not empty, pops item from stack and returns item.
           If stack is empty when pop is attempted, raises IndexError"""
        if self.is_empty():
            raise IndexError
        temp = self.items[num_items]
        self.items[num_items] = None
        return temp

    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
           If stack is empty, raises IndexError"""
        if self.is_empty():
            raise IndexError
        return self.items[num_items]

    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.num_items
 