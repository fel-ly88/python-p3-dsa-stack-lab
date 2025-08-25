class Stack:
    def __init__(self, items=None, limit=None):
        self.items = items if items is not None else []
        self.limit = limit

    def push(self, value):
        if self.limit is None or len(self.items) < self.limit:
            self.items.append(value)
        return self
    def pop(self):
        if not self.isEmpty():
            return self.items.pop()
        return None

    def peek(self):
        if not self.isEmpty():
            return self.items[-1]
        return None

    def size(self):
        return len(self.items)

    def isEmpty(self):
        return len(self.items) == 0

    def empty(self):
        return self.isEmpty()  # <-- fixes AttributeError

    def full(self):
        if self.limit is None:
            return False
        return len(self.items) >= self.limit

    def search(self, value):
        if value in self.items:
            # distance from top
            return len(self.items) - 1 - self.items.index(value)
        return -1



stack = Stack(limit=5)
stack.push(10).push(20).push(30)
print(stack.peek())   
print(stack.size())    
print(stack.search(20)) 
print(stack.full())    
stack.pop()
print(stack.peek())   
stack.clear = stack.items.clear() 
print(stack.empty())   
