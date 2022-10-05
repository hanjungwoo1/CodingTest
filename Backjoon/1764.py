N, M = map(int, input().split())

first = set()
second = set()

for _ in range(N):
    first.add(input())

for _ in range(M):
    second.add(input())


answer = list(first & second)

print(len(answer))

for name in sorted(answer):
    print(name)