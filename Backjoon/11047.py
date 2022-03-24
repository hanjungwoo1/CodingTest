n, k = map(int, input().split())
data = []
for _ in range(n):
    data.append(int(input()))

index = n-1
count = 0
while k!=0:
    count += k//data[index]
    k %= data[index]
    index -= 1

print(count)