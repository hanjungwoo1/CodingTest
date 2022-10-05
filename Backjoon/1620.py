import sys

input = sys.stdin.readline

N, M = map(int, input().split())

pocket_list = {}

for i in range(N):
    data = input().rstrip()
    pocket_list[i] = data
    pocket_list[data] = i


for _ in range(M):
    data = input().rstrip()

    if data.isdigit():
        print(pocket_list[int(data)-1])
    else:
        print(pocket_list[data]+1)