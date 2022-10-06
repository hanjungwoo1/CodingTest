import sys
from collections import defaultdict


input = sys.stdin.readline

T = int(input())


for _ in range(T):

    N = int(input())
    dict = defaultdict(list)
    for _ in range(N):
        item, category = input().split()
        dict[category].append(item)

    answer = 1
    for key, item in dict.items():
        answer *= (len(item)+1)

    print(answer-1)