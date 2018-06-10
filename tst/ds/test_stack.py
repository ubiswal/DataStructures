import unittest


from lib.ds.stack import Stack, StackOverflowException, StackUnderflowException


class TestStack (unittest.TestCase):
    def setUp(self):
        self.test_stack = Stack(5)
        
    def test_push_pop_stack(self):
        for i in range(0,3):
            self.test_stack.push(i)
        
        for i in range(2,-1,-1):
            self.assertEquals(i, self.test_stack.pop())

    def test_overflow_stack(self):
        for i in range(0,5):
            self.test_stack.push(i)
        self.assertRaises(StackOverflowException, self.test_stack.push, 10)
