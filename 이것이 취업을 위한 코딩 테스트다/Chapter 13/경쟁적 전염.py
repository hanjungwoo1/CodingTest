"""
입력 예시
3 3
1 0 2
0 0 0
3 0 0
2 3 2

출력 예시
3
"""


"""
입력 예시
3 3
1 0 2
0 0 0
3 0 0
1 2 2

출력 예시
0
"""


n, K = map(int, input().split())

graph = []
for _ in range(n):
    graph.append(list(map(int, input().split())))

s, X, Y = map(int, input().split())

# print("n, m : ", n, K)
# print(graph)
# print("s, x, y : ", s, X, Y)


# graph = [[0]*n for _ in range(m)]
# print(graph)


from collections import deque
dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

for second in range(1, s+1):

    for virus in range(1, K+1):

        for x in range(n):
            for y in range(n):
                if graph[x][y] == virus:
                    q = deque()
                    q.append([x, y, virus])

        while q:
            n_x, n_y, virus = q.popleft()
            for i in range(4):
             nx = n_x + dx[i]
             ny = n_y + dy[i]
             if nx >=0 and nx <n and ny>=0 and ny<n and graph[nx][ny] == 0:
                graph[nx][ny] = virus

    #print(second)


print(graph[X-1][Y-1])
