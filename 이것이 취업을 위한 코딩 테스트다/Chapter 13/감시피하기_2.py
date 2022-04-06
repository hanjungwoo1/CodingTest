"""
입력 예시 1
5
X S X X T
T X S X X
X X X X X
X T X X X
X X T X X

출력 예시 1
YES

입력 예시 2
4
S S S T
X X X X
X X X X
T T T X

출력 예시 2
NO
"""
n = int(input())

data = []
q = []
temp = [[0]*(n+1) for _ in range(n+1)]

for i in range(n):
    data.append(list(input().split()))
    for j in range(n):
        if data[i][j] =="T":
            q.append([i,j])

def check():
    for x, y in q:

        y_temp = y
        while y_temp >= 0:
            y_temp -= 1
            if temp[x][y_temp] == "O":
                break
            if temp[x][y_temp] == "S":
                return False

        y_temp = y
        while y_temp < n:
            y_temp += 1
            if temp[x][y_temp] == "O":
                break
            if temp[x][y_temp] == "S":
                return False

        x_temp = x
        while x_temp >= 0:
            x_temp -= 1
            if temp[x_temp][y] == "O":
                break
            if temp[x_temp][y] == "S":
                return False

        x_temp = x
        while x_temp >= n:
            x_temp += 1
            if temp[x_temp][y] == "O":
                break
            if temp[x_temp][y] == "S":
                return False
    return True

flag = False
def dfs(count):
    global flag
    if count == 3:
        for x in range(n):
            for y in range(n):
                temp[x][y] = data[x][y]

        if check():
            flag = True
        return

    for x in range(n):
        for y in range(n):
            if data[x][y] == "X":
                data[x][y] = "O"
                count += 1
                dfs(count)
                data[x][y] = "X"
                count -= 1

dfs(0)
if flag:
    print("YES")
else:
    print("NO")