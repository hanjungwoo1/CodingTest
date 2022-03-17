from collections import deque
import sys
n = int(sys.stdin.readline())

queue = deque()
for _ in range(n):
    data = sys.stdin.readline().split()

    if data[0] == 'push':
        queue.append(data[1])

    if data[0] == 'pop':
        if queue:
            print(queue.popleft())
        else:
            print(-1)

    if data[0] == 'size':
        print(len(queue))

    if data[0] == 'empty':
        if queue:
            print(0)
        else:
            print(1)

    if data[0] == 'front':
        if queue:
            print(queue[0])
        else:
            print(-1)

    if data[0] == 'back':
        if queue:
            print(queue[-1])
        else:
            print(-1)