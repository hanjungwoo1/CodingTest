import sys

input = sys.stdin.readline

N, M = map(int, input().split())

data = list(map(int, input().split()))

prefix_list = [0]

temp = 0
for each_data in data:
    temp += each_data
    prefix_list.append(temp)

for _ in range(M):
    x, y = map(int, input().split())
    print(prefix_list[y]-prefix_list[x-1])