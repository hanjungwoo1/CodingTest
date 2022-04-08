"""
입력 예시1
5
-15 -6 1 3 7

출력 예시1
3

입력 예시2
7
-15 -4 2 8 9 13 15

출력 예시2
2

입력 예시3
7
-15 -4 3 8 9 13 15

출력예시 3
-1
"""

def binary(array, target, start, end):
    if start>end:
        return None

    mid = (start + end) // 2

    if array[mid] == mid:
        return mid
    elif array[mid] > mid:
        return binary(array, target, start, mid-1)
    else:
        return binary(array, target, mid+1, end)



n = int(input())
data = list(map(int, input().split()))

result = binary(data, n//2, 0, n-1)

if result == None:
    print(-1)
else:
    print(result)