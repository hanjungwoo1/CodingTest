import sys

input = sys.stdin.readline

N, K = map(int, input().split())

answer = 1


for k in range(K):
    answer *= N
    answer /= k+1
    N = N-1


print(int(answer)*10007)