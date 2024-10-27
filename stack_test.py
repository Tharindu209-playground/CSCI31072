class Stack:
    def __init__(self):
        self.items = []

    def is_empty(self):
        return len(self.items) == 0

    def push(self, item):
        self.items.append(item)

    def pop(self):
        return self.items.pop() if not self.is_empty() else None

    def peek(self):
        return self.items[-1] if not self.is_empty() else None

def is_balanced_parentheses(expression):
    stack = Stack()
    pairs = {")": "(", "}": "{", "]": "["}

    for char in expression:
        if char in pairs.values():
            stack.push(char)
        elif char in pairs.keys():
            if stack.is_empty() or stack.pop() != pairs[char]:
                return False

    return stack.is_empty()

expression = "((2 + 3) * [5 - 4])"
print(f"Is balanced: {is_balanced_parentheses(expression)}")
