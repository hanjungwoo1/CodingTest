# from itertools import combinations, permutations
#
# import math
#
# def solution(n, k):
#     candidates = []
#     count = 0
#
#     for candi in permutations(list(range(1, n + 1)), n):
#         count += 1
#
#         if count == k:
#             return list(candi)

import math

def solution(n, k):
    Nums = list(range(1, n+1))
    Answer = []
    while n != 0:
        temp = math.factorial(n-1)
        Index, k = (k-1)//temp, k%temp
        Answer.append(Nums.pop(Index))
        n -= 1
    return Answer