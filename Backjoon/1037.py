import sys

input = sys.stdin.readline

N = int(input())

data_list = list(map(int, input().split()))

print(min(data_list) * max(data_list))