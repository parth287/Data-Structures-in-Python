class Stack:
    
    def __init__(self):
        self.items = []
    
    
    def push(self,item):
        self.items.append(item)
    
    def pop(self):
        return self.items.pop()
    
    def is_empty(self):
        return self.items == []

    def peek(self):
        if not self.is_empty():
            return self.items[-1]

    def __repr__(self):
        return f"{self.items}"


if __name__ == "__main__":
    
    s = Stack()
    s.push("A")
    s.push("B")
    s.push("C")
    s.push("D")
    print(s)
    s.pop()
    print(s)
    print(s.peek())



