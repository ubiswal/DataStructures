class StackOverflowException (Exception):
    pass


class StackUnderflowException (Exception):
    pass


class Stack:
    def __init__(self, max_size):
        self.storage = []
        self.top = -1
        self.max_size = max_size
    
    def push(self, val):
        if self.top+1 == self.max_size:
            raise StackOverflowException("Stack Overflow")
        self.storage.append(val)
        self.top = self.top+1
    
    def pop(self):
        if self.top == -1:
            raise StackUnderflowException("Stack Underflow")
        self.top = self.top -1
        return self.storage[self.top+1]
    
    def peek(self):
        return self.storage[self.top]