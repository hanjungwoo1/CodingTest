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
        if data[i] not in list:
            list.append(data[i])
            dfs(i+1)
            list.pop()

dfs(0)