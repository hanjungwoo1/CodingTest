from collections import deque, defaultdict


def solution(n, edge):
    visited = [0] * (n + 1)
    graph = defaultdict(list)

    for x, y in edge:
        graph[x].append(y)
        graph[y].append(x)

    queue = deque([1])
    visited[1] = 1

    while queue:

        now = queue.popleft()
        length = visited[now] + 1
        for end in graph[now]:

            if visited[end] == 0:
                visited[end] = length
                queue.append(end)

    return visited.count(max(visited[1:]))