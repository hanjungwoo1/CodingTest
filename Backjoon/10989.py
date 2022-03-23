# import sys
#
# n = int(sys.stdin.readline())
#
# data = []
# for _ in range(n):
#     data.append(int(sys.stdin.readline()))
#
# for x in sorted(data):
#     print(x)


import sys
n = int(sys.stdin.readline())
b = [0] * 10001
for i in range(n):
    b[int(sys.stdin.readline())] += 1
for i in range(10001):
    if b[i] != 0:
        for j in range(b[i]):
            print(i)