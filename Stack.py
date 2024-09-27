class Stack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)
        print(f"Pushed item: {item}")

    def pop(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack.pop()

    def peek(self):
        if self.is_empty():
            return "Stack is empty"
        return self.stack[-1]

    def size(self):
        return len(self.stack)


# Example usage
stack = Stack()
stack.push(1)
stack.push(2)
stack.push(3)
print(f"Popped item: {stack.pop()}")
print(f"Stack after popping an element: {stack.stack}")
print(f"Top item: {stack.peek()}")
print(f"Stack size: {stack.size()}")