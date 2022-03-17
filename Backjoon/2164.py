from collections import deque

queue = deque()

n = int(input())
for x in range(1, n+1):
    queue.append(x)

while len(queue)>1:
    queue.popleft()
    queue.append(queue.popleft())

print(queue.popleft())