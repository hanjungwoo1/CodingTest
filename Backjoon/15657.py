n, m = map(int, input().split())

data = list(map(int, input().split()))
data.sort()

k = len(data)

list = []
def dfs(start):
    if len(list) == m:
        print(' '.join(map(str, list)))
        return

    for i in range(start, k):
        list.append(data[i])
        dfs(i)
        list.pop()

dfs(0)