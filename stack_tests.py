import unittest

# Use the imports below to test either your array-based stack
# or your link-based version
from stack_array import Stack
from stack_linked import Stack

class TestLab2(unittest.TestCase):
    def test_simple(self):
        stack = Stack(5)
        self.assertRaises(IndexError, stack.pop)
        stack.push(0)
        self.assertFalse(stack.is_empty())
        self.assertFalse(stack.is_full())
        self.assertEqual(stack.size(),1)

    def test_simple_1(self):
        stack = Stack(3)
        self.assertRaises(IndexError, stack.peek)
        stack.push(0)
        stack.push(1)
        stack.push(2)
        self.assertRaises(IndexError, stack.push, 3)
        self.assertTrue(stack.is_full())
        self.assertEqual(stack.size(),3)
        stack.pop()
        stack.pop()
        self.assertEqual(stack.pop(), 0)


    def test_linked(self):
    	stack = Stack(10)
    	stack.push('a')
    	stack.pop()
    	self.assertEqual(stack.size(),0)
    	self.assertTrue(stack.is_empty())
    	stack.push('a')
    	stack.push('b')
    	stack.push('c')
    	stack.push('d')
    	stack.push('e')
    	stack.push('f')
    	stack.push('g')
    	stack.push('h')
    	stack.push('i')
    	stack.push('j')
    	self.assertTrue(stack.is_full())
    	self.assertRaises(IndexError, stack.push,'k')
    	stack.pop()
    	self.assertEqual(stack.peek(), 'i')
    	self.assertEqual(stack.size(), 9)

    def test_linked_1(self):
    	stack = Stack(4)
    	self.assertRaises(IndexError, stack.peek)
    	self.assertRaises(IndexError, stack.pop)
    	self.assertTrue(stack.is_empty())
    	self.assertFalse(stack.is_full())    	

if __name__ == '__main__': 
    unittest.main()
