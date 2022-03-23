n = int(input())

arr = []
for i in range(n):
    x, y = list(map(int, input().split()))
    arr.append([y, x])

arr.sort()

for k in range(n):
    print(arr[k][1], arr[k][0])