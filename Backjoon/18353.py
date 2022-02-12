import sys
f = sys.stdin.readline

n = int(f())
a = [int(x) for x in f().split()]
dp = [1] * n
# 앞쪽에 있는 값이 항상 뒤보다 커야함
# 남아있는 병사 수가 최대가 되어야 함

for i in range(n):
    for j in range(i):
        if a[i] < a[j]:
            dp[i] = max(dp[i], dp[j]+1)

print(len(a) - max(dp))