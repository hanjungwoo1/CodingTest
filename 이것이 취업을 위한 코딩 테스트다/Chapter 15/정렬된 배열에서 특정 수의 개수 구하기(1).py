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

###############################################################
# 시간초과 O(N)
###############################################################
# n, x = map(int, input().split())
# data = list(map(int, input().split()))
#
# answer = data.count(x)
#
# if answer == 0:
#     answer = -1
#
# print(answer)
###############################################################


###############################################################
# Solution : O(logN)
###############################################################
def count(array, x):

    n = len(array)

    a = l_binary(array, x, 0, n-1)

    if a == None:
        return 0

    b = r_binary(array, x, 0, n-1)

    return b-a+1


def l_binary(array, target, start, end):
    if start > end:
        return None

    mid = (start + end)//2

    if (mid == 0 or target > array[mid-1]) and array[mid] == target:
        return mid
    elif array[mid] >= target:
        return l_binary(array, target, start, mid - 1)
    else:
        return l_binary(array, target, mid + 1, end)

def r_binary(array, target, start, end):
    if start > end:
        return None

    mid = (start+end)//2

    if (mid == (n-1) or target < array[mid+1]) and array[mid] == target:
        return mid
    elif array[mid] > target:
        return r_binary(array, target, start, mid - 1)
    else:
        return r_binary(array, target, mid + 1, end)


n, x = map(int, input().split())
data = list(map(int, input().split()))

result = count(data, x)

if result == 0:
    print(-1)
else:
    print(result)
