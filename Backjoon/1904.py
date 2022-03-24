import sys

n = int(sys.stdin.readline())

dp = [0] * 1000001
#dp = [0] * (n+1)   --> 런타임 에러


dp[1] = 1
dp[2] = 2

# 피보나치 수열 형태로 진행
for i in range(3, n+1):
    dp[i] = (dp[i-1] + dp[i-2]) % 15746
    
print(dp[n])
