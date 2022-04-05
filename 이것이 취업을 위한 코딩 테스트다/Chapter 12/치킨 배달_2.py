from itertools import combinations

n, m = map(int, input().split())

graph = []

for _ in range(n):
    graph.append(list(map(int, input().split())))

print(n, m)
print(graph)

home = []
chicken = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 1:
            home.append([x, y])

        if graph[x][y] == 2:
            chicken.append([x, y])

print(home)
print(chicken)


result = 1e9
for chicken_m in combinations(chicken, m):
    total = 0
    for house in home:
        dist = 1e9
        # each 1 house
        for chick in chicken_m:
            distance = abs(chick[0] - house[0]) + abs(chick[1] - house[1])
            dist = min(dist, distance)      # 최소 치킨집 거리

        total += dist
    result = min(result, total)

print(result)