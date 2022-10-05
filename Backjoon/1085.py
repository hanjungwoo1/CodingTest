import sys

input = sys.stdin.readline

x, y, w, h = map(int, input().rstrip().split())

result = min([x, y, w-x, h-y])
print(result)