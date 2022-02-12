# """
# 입력 예시
# 7
# 15 11 4 8 5 2 4
# """
#


# n = int(input())
#
# data = list(map(int, input().split()))
#
# count = 0
# temp = 1e9
# for x in data:
#     if temp > x:
#         temp = x
#     else:
#         count = count + 1
#         temp = x
#
# print(count)


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