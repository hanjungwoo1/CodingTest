N = int(input())

stair = [0]
for _ in range(N):
    stair.append(int(input()))

if N == 1:
    print(stair[1])
else:
    dp = [0] * (N+1)
    dp[1] = stair[1]
    dp[2] = stair[1] + stair[2]

    for i in range(3, N+1):
        dp[i] = max(dp[i-3]+stair[i-1]+stair[i], dp[i-2]+stair[i])

    print(dp[N])

# i 일때,
# 밟은 계단이 i-1일 경우 i-2는 밟으면 안된다
# 밟은 계단이 i-2일 경우 그 전 계단은 신경쓰지 않는다