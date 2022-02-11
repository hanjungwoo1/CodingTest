def dfs(n, computers, start, visited):
    visited[start] = True

    for i in range(n):
        if (visited[i] == False and computers[start][i] == 1):
            dfs(n, computers, i, visited)


def solution(n, computers):
    visited = [False] * n
    answer = 0

    for start in range(n):
        if (visited[start] == False):
            dfs(n, computers, start, visited)
            answer += 1

    return answer