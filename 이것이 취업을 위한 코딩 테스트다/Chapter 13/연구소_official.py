"""
입력 예시
4 6
0 0 0 0 0 0
1 0 0 0 0 2
1 1 1 0 0 2
0 0 0 0 0 2

"""
def virus(x, y):
    for i in range(4):
        nx = x+dx[i]
        ny = y+dy[i]
        if nx >= 0 and nx < N and ny >= 0and ny < M :
            if temp[nx][ny] == 0:
                temp[nx][ny] = 2
                virus(nx, ny)

def get_score():
    score = 0
    for i in range(N):
        for j in range(M):
            if temp[i][j] == 0:
                score += 1
    return score



N, M = map(int, input().split())

data = []
temp = [[0]*M for _ in range(N)]

for _ in range(N):
    data.append(list(map(int, input().split())))


dx = [-1, 1, 0, 0]
dy = [0, 0, -1, 1]

result = 0
def dfs(count):
    global result

    if count == 3:
        for i in range(N):
            for j in range(M):
                temp[i][j] == data[i][j]

        for i in range(N):
            for j in range(M):
                if temp[i][j] == 2:
                    virus(i, j)

        result = max(result, get_score())
        return

    for i in range(N):
        for j in range(M):
            if data[i][j] == 0:
                data[i][j] = 1
                count += 1
                dfs(count)
                data[i][j] = 0
                count -= 1

dfs(0)
print(result)