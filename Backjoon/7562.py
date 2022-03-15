from collections import deque


t = int(input())

for i in range(t):
    k = int(input())
    graph = [[0]*k for _ in range(k)]
    x, y = map(int, input().split())
    m, n = map(int, input().split())


    dx = [-2, -1, 1, 2, 2, 1, -1, -2]
    dy = [1, 2, 2, 1, -1, -2, -2, -1]

    queue = deque()
    queue.append([x, y])
    graph[x][y] = 1
    while queue:
        a, b = queue.popleft()
        if a == m and b == n:
            print(graph[a][b]-1)

        for i in range(8):
            nx = a+dx[i]
            ny = b+dy[i]

            if 0 <= nx < k and 0 <= ny < k and graph[nx][ny] == 0:
                graph[nx][ny] = graph[a][b] + 1
                queue.append([nx, ny])