"""
입력 예시 1
7 2
1 1 2 2 2 2 3

출력 예시 1
4

입력 예시 2
7 4
1 1 2 2 2 2 3

출력 예시 2
-1
"""


from bisect import bisect_left, bisect_right

n, x = map(int, input().split())
data = list(map(int, input().split()))

left = bisect_left(data, x)

if left == n:
    print(-1)
else:
    right = bisect_right(data, x)
    print(right - left)

print(left, right)