import sys
input = sys.stdin.readline


data = [1,2,3,4,5,6,7,8,9,10] # n -> n/2 -> O(n)
key = 8

# 순차 탐색, Sequential Searching (정렬X) -> O(n)
for inner_data in data:
    if inner_data == key:
        print("find", key)

# 이진 탐색, Binary Searching (정렬O) -> O(logN)

# def binary_Searching(array, key, start, end):
def binary_Searching(array:list, key:int, start:int, end:int)-> int:
    while start <= end:
        mid = (start + end) // 2

        print(mid, array)
        if array[mid] == key:
            return mid
        elif array[mid] > key:
            end = mid - 1
        else:
            start = mid + 1
    return None

print(binary_Searching(data, key, 0, len(data)))

# Hash -> O(1) 가.500.23-1 (32책장, 위에서 3번째칸, 왼쪽에서 4)

