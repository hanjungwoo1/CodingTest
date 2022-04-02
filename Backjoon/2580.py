import sys

graph = []
zero = []
for i in range(9):
    graph.append(list(map(int, sys.stdin.readline().split())))

for i in range(9):
    for j in range(9):
        if graph[i][j] == 0:
            zero.append([i, j])

def checkrow(x, a):
    for i in range(9):
        if a == graph[x][i]:
            return False
    return True

def checkcol(y, a):
    for i in range(9):
        if a == graph[i][y]:
            return False
    return True

def checkRect(x, y, a):
    nx = x // 3 * 3
    ny = y // 3 * 3
    for i in range(3):
        for j in range(3):
            if a == graph[nx+i][ny+j]:
                return False
    return True

def dfs(idx):
    if idx == len(zero):
        for i in range(9):
            print(*graph[i])
        exit(0)

    for i in range(1, 10):
        x = zero[idx][0]
        y = zero[idx][1]

        if checkrow(x, i) and checkcol(y, i) and checkRect(x, y, i):
            graph[x][y] = i
            dfs(idx+1)
            graph[x][y]=0

dfs(0)