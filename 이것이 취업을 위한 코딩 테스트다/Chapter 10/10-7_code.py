"""
입력 예시
7 8
0 1 3
1 1 7
0 7 6
1 7 1
0 3 7
0 4 2
0 1 1
1 1 1
"""



def find_parent(parent, x):
    if parent[x] != x:
        return find_parent(parent, parent[x])
    return x

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)
    if a < b:
        parent[b] = a
    else:
        parent[a] = b

n, m = map(int, input().split())

parent = [0] * (n+1)

for i in range(n+1):
    parent[i] = i

for i in range(m):
    x, y, z = map(int, input().split())
    if x == 0:
        union_parent(parent, y, z)
    elif x == 1:
        if find_parent(parent, y) == find_parent(parent, z):
            print("YES")
        else:
            print("NO")
    else:
        print("error")