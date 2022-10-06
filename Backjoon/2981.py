import sys
from math import gcd

n = int(sys.stdin.readline())
ls = []
result = []

for _ in range(n):
    ls.append(int(sys.stdin.readline()))
ls.sort()  # 오른차순 정렬

temp = [ls[i] - ls[i - 1] for i in range(1, n)]  # 각 인접 요소들끼리 뺄셈
my_gcd = temp[0]  # 리스트 내 모든 요소들의 gcd를 구하기 위함

for i in range(1, n - 1):
    my_gcd = gcd(my_gcd, temp[i])

for i in range(1, int(pow(my_gcd, 1 / 2)) + 1):

    if my_gcd % i == 0:
        if i ** 2 == my_gcd:
            result.append(i)
        else:
            result += [i, my_gcd // i]
result.remove(1)
result.sort()

for i in range(len(result)):
    print(result[i], end=" ")