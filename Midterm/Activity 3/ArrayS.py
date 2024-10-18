class ArrayStack:
    def __init__(self):
        self.stack = []

    def is_empty(self):
        return len(self.stack) == 0

    def push(self, item):
        self.stack.append(item)

    def pop(self):
        if not self.is_empty():
            return self.stack.pop()
        raise IndexError("pop from empty stack")


class ParenthesesMatcher:
    def __init__(self):
        self.stack = ArrayStack()

    def is_matched(self, expression):
        matching_parentheses = {')': '(', '}': '{', ']': '['}

        for char in expression:
            if char in matching_parentheses.values():
                self.stack.push(char)
            elif char in matching_parentheses.keys():
                if self.stack.is_empty() or self.stack.pop() != matching_parentheses[char]:
                    return False

        return self.stack.is_empty()

class FileReverser:
    @staticmethod
    def reverse_file(filename):
        stack = ArrayStack()


        with open(filename, 'r') as file:
            for line in file:
                stack.push(line.rstrip('\n'))


        with open(filename, 'w') as file:
            while not stack.is_empty():
                file.write(stack.pop() + '\n')