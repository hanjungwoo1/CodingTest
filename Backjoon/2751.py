import sys
n = int(input())
l = []
for i in range(n):
    l.append(int(sys.stdin.readline()))
for i in sorted(l):
    sys.stdout.write(str(i)+'\n')

## 시간초과
# n = int(input())
# l = []
# for i in range(n):
#     l.append(int(input()))
# for i in sorted(l):
#     print(i)
