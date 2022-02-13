n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

k = len(data)

list = []
def dfs():
    if len(list) == m:
        print(' '.join(map(str, list)))
        return

    for i in range(0, k):
        list.append(data[i])
        dfs()
        list.pop()

dfs()