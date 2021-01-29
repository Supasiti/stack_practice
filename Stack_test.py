import unittest
from Stack import Stack

class TestStack(unittest.TestCase):

    def setUp(self):
        self.stack = Stack()
    
    def tearDown(self):
        self.stack = None

    def test_push_once(self):
        self.stack.push(1)

        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(1 in self.stack, True)
        self.assertEqual(2 in self.stack, False)

    def test_push_twice(self):
        self.stack.push(1)
        self.stack.push(2)

        self.assertEqual(self.stack.peek(), 2)
        self.assertEqual(len(self.stack), 2)
        self.assertEqual(1 in self.stack, True)

    def test_push_pop(self):
        self.stack.push(1)
        result = self.stack.pop()

        self.assertEqual(self.stack.peek(), None)
        self.assertEqual(len(self.stack), 0)
        self.assertEqual(result, 1)
        self.assertEqual(1 in self.stack, False)

    def test_push_twice_pop(self):
        self.stack.push(1)
        self.stack.push(2)
        result = self.stack.pop()

        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(result, 2)
        self.assertEqual(1 in self.stack, True)
        self.assertEqual(2 in self.stack, False)

    def test_push_thrice_clear(self):
        self.stack.push(1)
        self.stack.push(2)
        self.stack.push(3)
        self.stack.clear()

        self.assertEqual(self.stack.peek(), None)
        self.assertEqual(len(self.stack), 0)
        self.assertEqual(1 in self.stack, False)
    
    def test_pop(self):
        with self.assertRaises(IndexError): 
            self.stack.pop()   

    def test_loop_through_stack(self):
        self.stack = Stack([1,2,3])

        num_list = [i for i in self.stack]
        self.assertEqual(num_list, [3,2,1])
    
    def test_arithmetic_add(self):
        self.stack += 1
        
        self.assertEqual(self.stack.peek(), 1)
        self.assertEqual(len(self.stack), 1)
        self.assertEqual(1 in self.stack, True)
        self.assertEqual(2 in self.stack, False)

if __name__ == "__main__":
    unittest.main()