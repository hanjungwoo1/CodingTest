from collections import deque
def solution(maps):
    n = len(maps); m = len(maps[0])
    visited = [[False]*m for _ in range(n)]
    q = deque()
    q.append((0, 0))
    dx = [-1, 1, 0, 0]
    dy = [0, 0, -1, 1]
    visited[0][0]=True
    while q:
        y, x = q.popleft()
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<m and 0<=ny<n and maps[ny][nx] == 1:
                if not visited[ny][nx]:
                    visited[ny][nx] = True
                    q.append((ny, nx))
                    maps[ny][nx] = maps[y][x]+1
    if maps[n-1][m-1]==1:
        return -1
    else:
        return maps[n-1][m-1]