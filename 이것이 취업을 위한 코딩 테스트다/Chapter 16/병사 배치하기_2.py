"""
7
15 11 4 8 5 2 4
"""
n = int(input())

data = list(map(int, input().split()))

dp = [1] * n

print(n)
print(data)

for i in range(n):
    for j in range(i):
        if data[i] < data[j]:
            print(data[i], data[j])
            dp[i] = max(dp[i], dp[j]+1)

    print(dp)

print(n-max(dp))