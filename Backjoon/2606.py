import sys

n = int(sys.stdin.readline())  # 컴퓨터의 수
m = int(sys.stdin.readline())  # 간선의 수

graph = [[] for _ in range(n+1)]

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    graph[a].append(b)
    graph[b].append(a)

visited = [0] * (n+1)

def dfs(v):
    visited[v] = 1

    for x in graph[v]:
        if not visited[x]:
            dfs(x)

dfs(1)

print(sum(visited)-1)