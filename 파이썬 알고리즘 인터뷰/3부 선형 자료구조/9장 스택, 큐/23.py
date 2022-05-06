from collections import deque

class MyStack():
    def __init__(self):
        self.q = deque()

    def push(self, data):
        self.q.append(data)

    def pop(self):
        data = self.q.pop()
        return data

    def top(self):
        data = self.q.pop()
        self.q.append(data)
        return data

    def empty(self):
        return len(self.q) == 0

stack = MyStack()
stack.push(1)
stack.push(2)
print(stack.top())
print(stack.pop())
print(stack.empty())