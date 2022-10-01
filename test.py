# A = [4, 7, 1, 5, 3]
# A = [12, 12, 12, 15, 10]
# A = [18, 26, 18, 24, 24, 20, 22]
#
# A = sorted(A)
# total_count = 0
# print(A)
#
# for step in range(0, 5):
#
#     if step != 0:
#         A = list(set(A))
#
#     length = len(A)
#
#     step_count = 1
#     for i in range(length):
#         for j in range(i+1, length):
#                 if A[j] - A[i] == step:
#                     print(A[i], A[j], step)
#                     step_count +=1
#                     break
#         print("result : ", step, step_count)
#     total_count = max(total_count, step_count)
#
# print(total_count)

def mark(graph, x, y, N, M, Direction):
    if x < 0 or N <= x:
        return graph

    if y < 0 or M <= y:
        return graph

    if graph[x][y] in ['X', '<', '>', '^', 'v']:
        return graph

    graph[x][y] = 'o'

    if Direction == "right":
        mark(graph, x, y+1, N, M, "right")

    if Direction == "left":
        mark(graph, x, y-1, N, M, "left")

    if Direction == "down":
        mark(graph, x+1, y, N, M, "down")

    if Direction == "up":
        mark(graph, x-1, y, N, M, "up")

    return graph

def check_guard(graph, N, M):

    start = [-1, -1]

    for x in range(N):
        for y in range(M):
            if graph[x][y] == "A":
                start = [x, y]

            if graph[x][y] == ">":
                graph[x][y] = 'o'
                graph = mark(graph, x, y+1, N, M, "right")

            if graph[x][y] == "<":
                graph[x][y] = 'o'
                graph = mark(graph, x, y-1, N, M, "left")

            if graph[x][y] == "v":
                graph[x][y] = 'o'
                graph = mark(graph, x+1, y, N, M, "down")

            if graph[x][y] == "^":
                graph[x][y] = 'o'
                graph = mark(graph, x-1, y, N, M, "up")

    return start

from collections import deque


first = [0, 0, 1, -1]
second = [-1, 1, 0, 0]


def bfs(graph, start, N, M):

    queue = deque([start])
    graph[start[0]][start[1]] = 'G'

    while queue:
        cur = queue.popleft()

        i = cur[0]
        j = cur[1]

        for x, y in zip(first, second):
            new_x = i+x
            new_y = j+y

            if new_x < 0 or new_x >=N or new_y < 0 or new_y >= M:
                continue
            elif graph[new_x][new_y] == ".":
                queue.append([new_x, new_y])
                graph[new_x][new_y] = 'G'

    return graph




data = ['X.....>', '..v..X.', '.>..X..', 'A......']
# data = ['...Xv', 'AX..^', '.XX..']
# data = ['...', '>.A']
# data = ['A.v', '...']

N = len(data)
M = len(data[0])
print(N, M)

graph = [[0 for col in range(M)] for row in range(N)]

for i, row in enumerate(data):
    for j, column in enumerate(row):
        graph[i][j] = column

print(graph)
start = check_guard(graph, N, M)
print("start : ", start)
print(graph)

if start == (-1, -1):
    print("false")

graph = bfs(graph, start, N, M)

print(graph)
print(graph[0][0])
if graph[N-1][M-1] == "G":
    return True
else:
    return False