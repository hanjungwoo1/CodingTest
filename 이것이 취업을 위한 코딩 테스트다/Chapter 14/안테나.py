"""
입력 예시 1
4
5 1 7 9

출력 예시 1
5
"""


# n = int(input())
#
# antena = sorted(list(map(int, input().split())))
#
# result = 1e9
# flag = 0
# for x in antena:
#     total = 0
#     for y in antena:
#         if x ==y :
#             continue
#         length = abs(x-y)
#         total += length
#
#     if result > total:
#         result = total
#         flag = x
# print(flag)

n = int(input())

antena = sorted(list(map(int, input().split())))

# 중간값이 항상 제일 좋음
print(antena[(n-1)//2])