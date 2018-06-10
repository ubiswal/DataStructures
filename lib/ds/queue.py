class Queue:
    def __init__(self):
        self.storage = []
    
    def push(self, val):
        self.storage.append(val)
            
    def pop(self):
        if len(self.storage) == 0:
            return Exception("Queue is empty!")
        ret_val = self.storage[0]
        del self.storage[0]
        return ret_val