from collections import deque

def bfs(v):
    q = deque()
    q.append(v)
    visited[v] = 1

    while q:
        v = q.popleft()
        print(v, end = " ")
        for i in graph[v]:
            if not visited[i]:
                q.append(i)
                visited[i] = True

def dfs(v):
    print(v, end=" ")
    visited[v] = 1
    for i in graph[v]:
        if not visited[i]:
            dfs(i)

N, M, V = map(int, input().split())

graph = [[] for _ in range(N+1)]
visited = [0] * (N+1)

for _ in range(M):
    a, b = map(int, input().split())
    graph[a].append(b)
    graph[b].append(a)

for i in range(1, N+1):
    graph[i].sort()

dfs(V)

visited = [0] * (N+1)
print()
bfs(V)

