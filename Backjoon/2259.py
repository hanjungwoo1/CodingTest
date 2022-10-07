# import sys
#
# input = sys.stdin.readline
#
# N, M = map(int, input().split())
#
# data = list(map(int, input().split()))
#
# temp = 0
# M_count = M
# answer = 0
# for i, each_data in enumerate(data):
#
#     temp += each_data
#     if M_count == 0:
#         temp -= data[i-M]
#     else:
#         M_count -= 1
#
#     answer = max(temp, answer)
#
# print(answer)


import sys

input = sys.stdin.readline

n, k = map(int, input().split())
a = list(map(int, input().split()))

result = []
result.append(sum(a[:k]))

for i in range(n - k):
    result.append(result[i] - a[i] + a[k + i])

print(max(result))