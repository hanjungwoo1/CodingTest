import sys, math

input = sys.stdin.readline

T = int(input())


for _ in range(T):
    left, right = map(int, input().split())
    print(math.lcm(left, right))

