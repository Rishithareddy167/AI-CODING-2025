class Stack:
    def __init__(self):
        self._items = []

    def push(self, item):
        self._items.append(item)

    def pop(self):
        if self.is_empty():
            raise IndexError("Pop from empty stack")
        return self._items.pop()

    def peek(self):
        if self.is_empty():
            raise IndexError("Peek from empty stack")
        return self._items[-1]

    def is_empty(self):
        return len(self._items) == 0

if __name__ == "__main__":
    stack = Stack()
    stack.push(10)
    stack.push(20)
    stack.push(30)

    print("Top element (peek):", stack.peek())   
    print("Popped element:", stack.pop())        
    print("Popped element:", stack.pop())        
    print("Is stack empty?", stack.is_empty())   
    print("Popped element:", stack.pop())        
    print("Is stack empty?", stack.is_empty())