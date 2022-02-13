n = int(input())

data = sorted(list(map(int, input().split())), reverse=True)

count = 0
while True:
    if len(data)==0:
        break

    k = data[0]
    if len(data) >= k:
        data = data[k:]
        count += 1
    elif len(data) < k:
        break

print(count)