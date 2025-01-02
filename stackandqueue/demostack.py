class Stack:
    def __init__(self):
        self.stack = []

    def push(self, data):
        if len(self.stack) < 10:
            self.stack.append(data)
        else:
            print("Error: StackOverFlow stack is full")

    def pop(self):
        if len(self.stack) == 0:
            return "Error: StackUnderFlow stack is empty"
        return self.stack.pop()

    def peak(self):
        if len(self.stack) == 0:
            return "Error: StackUnderFlow stack is empty"
        return self.stack[-1]

    def is_empty(self):
        return len(self.stack) == 0

    def size(self):
        return len(self.stack)


s1 = Stack()
print(s1.size())
print(s1.is_empty())
print(s1.peak())
print(s1.pop())
for i in range(10):
    s1.push(i)
print(s1.stack)
print(s1.pop())
print(s1.pop())
s1.push(999)
s1.push(888)
print(s1.stack)
s1.push(777)
