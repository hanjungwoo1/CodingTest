"""
입력

0 1 2 2 2 7
"""

chess_list = [1, 1, 2, 2, 2, 8]

input_count = list(map(int, input().split()))

for x, y in zip(chess_list, input_count):
    print(x-y, end=" ")