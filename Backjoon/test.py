from itertools import combinations

N, M = map(int, input().split())

data = [x for x in range(1,N+1)]

result = list(combinations(data, M))

for x in result:
    print(x)