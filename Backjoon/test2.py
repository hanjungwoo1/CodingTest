n, m = map(int, input().split())

s = []


def dfs(start):
    if len(s) == m:
        print(' '.join(map(str, s)))

        return

    for i in range(start, n+1):

        print("start : ", start, "i : ", i," list : ", s)
        if i not in s:
            s.append(i)
            print("append :", s)
            dfs(i+1)
            s.pop()

dfs(1)
