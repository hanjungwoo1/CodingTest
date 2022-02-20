from itertools import combinations


"""
입력 예시 1
5 3
0 0 1 0 0
0 0 2 0 1
0 1 2 0 0
0 0 1 0 0
0 0 0 0 2

출력 예시 1
5

입력 예시 2
5 2
0 2 0 1 0
1 0 1 0 0
0 0 0 0 0
2 0 0 1 1
2 2 0 1 2

출력 예시2
10

입력 예시3
5 1
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0
1 2 0 0 0

출력 예시 3
11
"""

n, m = map(int, input().split())

graph = []

for _ in range(n):
    temp = list(map(int, input().split()))
    graph.append(temp)

chicken = []
houses = []

for x in range(n):
    for y in range(n):
        if graph[x][y] == 2:
            chicken.append([x,y])
            graph[x][y] = 4

        if graph[x][y] == 1:
            houses.append([x,y])
            graph[x][y] = 5


chicken_list = combinations(chicken, m)


result = 1e9
for chicken_m in chicken_list:
    total = 0
    for house in houses:
        dist = 1e9
        # each 1 house
        for chick in chicken_m:
            distance = abs(chick[0] - house[0]) + abs(chick[1] - house[1])
            dist = min(dist, distance)      # 최소 치킨집 거리

        total += dist
    result = min(result, total)

    # for chic in chicken_m:
    #     # chic -> chicken position with m
    #     for hou in house:
    #         distance = abs(chic[0] - hou[0]) + abs(chic[1] - hou[1])
    #         print(distance)
    #         total = min(distance, total)

print(result)



