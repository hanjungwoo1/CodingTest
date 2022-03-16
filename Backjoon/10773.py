import sys

n = int(sys.stdin.readline())

arr = []

for _ in range(n):
    x = int(sys.stdin.readline())
    if x == 0:
        del arr[-1]
    else:
        arr.append(x)

    #print(arr)

print(sum(arr))
