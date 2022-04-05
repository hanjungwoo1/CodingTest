"""
5
2 3 1 2 2

2
"""


n = int(input())

data = list(map(int, input().split()))
data.sort()
print(data)

count = 0
result = 0

for x in data:
    count += 1
    if count >= x:
        result += 1
        count =0
    #print(x, count, result)

print(result)

