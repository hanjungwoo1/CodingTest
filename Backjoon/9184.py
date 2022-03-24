MAX = 21
dp = [[[0]*MAX for _ in range(MAX)] for _ in range(MAX)]

# print(len(dp))
# print(len(dp[0]))
# print(len(dp[0][0]))
# print(dp[0][0][0])

def w(a, b, c):
    if a <= 0 or b <= 0 or c <= 0:
        return 1

    if a > 20 or b > 20 or c > 20:
        return w(20, 20, 20)

    if dp[a][b][c]:
        return dp[a][b][c]

    elif a < b and b < c :
        dp[a][b][c] =  w(a, b, c-1) + w(a, b-1, c-1) - w(a, b-1, c)
        return dp[a][b][c]

    dp[a][b][c] = w(a-1, b, c) + w(a-1, b-1, c) + w(a-1, b, c-1) - w(a-1, b-1, c-1)
    return dp[a][b][c]

while True:
    a, b, c = map(int, input().split())
    if a == -1 and b == -1 and c == -1:
        break
    result = w(a, b, c)
    print("w({0}, {1}, {2}) = {3}".format(a, b, c, result))