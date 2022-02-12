"""
2
3 4
1 3 3 2 2 1 4 1 0 6 4 7
4 4
1 3 1 5 2 2 4 1 5 0 2 3 0 6 1 2
"""


for tc in range(int(input())):

    n, m = map(int, input().split())
    data = list(map(int, input().split()))

    graph = []
    index = 0
    for i in range(n):
        graph.append(data[index:index+m])
        index += m

    print(graph)




