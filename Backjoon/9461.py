import sys
dp = [0] * 101

dp[1] = 1
dp[2] = 1
dp[3] = 1
dp[4] = 2
dp[5] = 2

for i in range(5, 101):
    dp[i] = dp[i - 1] + dp[i - 5]

n = int(sys.stdin.readline())

for _ in range(n):
    x = int(sys.stdin.readline())
    print(dp[x])