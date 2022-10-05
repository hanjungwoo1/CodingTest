import sys

input = sys.stdin.readline

n = int(input())
arr = []
maxx = [(0, 0), (0, 0)]
# 큰 사각형의 변을 구한다
for i in range(6):
    d, w = map(int, input().split())
    d = 0 if d <= 2 else 1
    if w > maxx[d][1]:
        maxx[d] = (i, w)
    arr.append((d, w))

# 인접한 변들을 체크해준다.
ans = maxx[0][1] * maxx[1][1]
check = [False] * 6
for idx, _ in maxx:
    for i in idx, (idx + 1) % 6, idx - 1:
        check[i] = True

# 체크되지 않은 남은 변을 찾아 넓이를 빼 준다.
min_square = 1
for i in range(6):
    if not check[i]:
        min_square *= arr[i][1]
print((ans - min_square) * n)