class MyQueue:
    def __init__(self):
        self.input = []
        self.output = []

    def push(self, x):
        self.input.append(x)

    def pop(self):
        self.peek()
        return self.output.pop()

    def peek(self):
        # output이 없으면 모두 재입력
        if not self.output:
            while self.input:
                self.output.append(self.input.pop())
        return self.output[-1]

    def empty(self):
        return self.input == [] and self.output == []


q = MyQueue()
q.push(1)
q.push(2)

print(q.input)
print(q.output)

print(q.peek())
print(q.input)
print(q.output)

print(q.peek)
print(q.input)
print(q.output)




