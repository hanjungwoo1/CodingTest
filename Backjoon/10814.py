n = int(input())

data = []

for _ in range(n):
    x, y = map(str, input().split())
    data.append([int(x), y])

sorted_data = sorted(data, key=lambda item : item[0])

for x, y in sorted_data:
    print('{0} {1}'.format(x, y))