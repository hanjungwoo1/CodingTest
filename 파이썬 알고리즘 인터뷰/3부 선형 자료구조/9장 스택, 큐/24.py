class MyQueue():
    def __init__(self):
        self.left = []
        self.right = []

    def push(self, data):
        self.left.append(data)


queue = MyQueue()

queue.push(1)
queue.push(2)
