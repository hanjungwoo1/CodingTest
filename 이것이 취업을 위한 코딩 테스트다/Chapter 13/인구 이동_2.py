"""
입력 예시 1
2 20 50
50 30
20 40

출력 예시 1

입력 예시 2
2 40 50
50 30
20 40

출력 예시 2
0

입력 예시 3
2 20 50
50 30
30 40

출력 예시 3
1

입력 예시  4
3 5 10
10 15 20
20 30 25
40 22 10

출력 예시 4
2

입력 예시 5
4 10 50
10 100 20 90
80 100 60 70
70 20 30 40
50 20 100 10


출력 예시 5
3

"""


n, l, r = map(int, input().split())

graph = []


for _ in range(n):
    graph.append(list(map(int, input().split())))

temp = [[-1]*n for _ in range(n)]
temp[0][0] = 0

print(n, l, r)
print(graph)

dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

def check(x, y):

    for i in range(n):
        nx = x + dx[i]
        ny = y + dy[i]

        if nx >= 0 and nx < n and ny >= 0 and ny < n:
            # 여기서 확인 해야함, 국경선 열지
            value = abs(graph[x][y] - graph[nx][ny])
            if l <= value and value < r:

                # -1이면 내껄 주고, -1이 아니면 상대껄 가져오고,
                if temp[nx][ny] == -1:
                    temp[nx][ny] = temp[x][y]
                else:
                    temp[x][y] = temp[nx][ny]
            else:
                temp[nx][ny] = temp[x][y] + 1




for i in range(n):
    for j in range(n):
        check(i, j)

print(temp)