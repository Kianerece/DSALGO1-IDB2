class LinkedStack:
    class Node:
        def __init__(self, data=None, next_node=None):
            self.data = data
            self.next = next_node

    def __init__(self):
        self.top = None
        self.size = 0

    def push(self, item):
        new_node = self.Node(item, self.top)  # Create a new node with the item
        self.top = new_node                    # Set the new node as the top of the stack
        self.size += 1

    def pop(self):
        if self.is_empty():
            raise IndexError("pop from empty stack")
        data = self.top.data
        self.top = self.top.next              # Set the next node as the new top
        self.size -= 1
        return data

    def peek(self):
        if self.is_empty():
            raise IndexError("peek from empty stack")
        return self.top.data

    def is_empty(self):
        return self.size == 0

    def __str__(self):
        items = []
        current = self.top  # Start from the top node
        while current:      # Loop until we reach the end (None)
            items.append(str(current.data))  # Append the data of each node
            current = current.next           # Move to the next node
        return " -> ".join(items)  # Join all items into a string