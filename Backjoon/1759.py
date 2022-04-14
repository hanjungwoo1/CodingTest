from itertools import combinations

vowels = ('a', 'e', 'i', 'o', 'u')
n, m = map(int, input().split())
data = list(input().split())
data.sort()

for x in combinations(data, n):
    count = 0
    for y in x:
        if y in vowels:
            count += 1

    if count >= 1 and count <= n -2:
        print(''.join(x))