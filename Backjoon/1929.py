"""
입력 예시
3 16

출력 예시
3
5
7
11
13
"""
import math

left, right = map(int, input().split())
array = [True for i in range(right+1)]
array[1] = 0

for i in range(2, int(math.sqrt(right)) + 1):
    if array[i] == True:
        j = 2
        while i * j <= right:
            array[i * j] = False
            j += 1

for i in range(left, right+1):
    if array[i]:
        print(i)