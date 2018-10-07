class Node:
    def __init__(self, data):
        self.data = data
        self.next = None

class Stack:
    """Implements an efficient last-in first-out Abstract Data Type using a Linked List"""

    def __init__(self, capacity):
        """Creates and empty stack with a capacity"""
        self.capacity = capacity
        self.head = None
        self.count = 0

    def is_empty(self):
        """Returns True if the stack is empty, and False otherwise"""
        if self.head == None:
            return True
        return False

    def is_full(self):
        """Returns True if the stack is full, and False otherwise"""
        if self.count == self.capacity:
            return True
        return False

    def push(self, item):
        """If stack is not full, pushes item on stack. 
        If stack is full when push is attempted, raises IndexError"""
        if self.is_full():
            raise IndexError
        newNode = Node(item)
        newNode.next = self.head
        self.head = newNode
        self.count += 1

    def pop(self): 
        """If stack is not empty, pops item from stack and returns item.
        If stack is empty when pop is attempted, raises IndexError"""
        if self.is_empty():
            raise IndexError
        returnvalue = self.head.data
        self.head = self.head.next
        self.count -= 1
        return returnvalue

    def peek(self):
        """If stack is not empty, returns next item to be popped (but does not pop the item)
        If stack is empty, raises IndexError"""
        if self.is_empty():
            raise IndexError
        return self.head.data
    def size(self):
        """Returns the number of elements currently in the stack, not the capacity"""
        return self.count
 